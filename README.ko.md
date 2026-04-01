# Korean NOTAM API and Crawler

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

[![CI](https://github.com/allofdaniel/korean-notam-api/actions/workflows/ci.yml/badge.svg)](https://github.com/allofdaniel/korean-notam-api/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

한국 NOTAM 데이터를 수집, 정규화, 모니터링하고 자체 호스팅까지 할 수 있게 해주는 오픈소스 Python 도구 모음입니다.

한국에는 개발자가 바로 쓰기 쉬운 공개형 NOTAM API가 사실상 없습니다. 이 저장소는 다운스트림 팀이 반복해서 다시 만들게 되는 핵심 레이어를 묶어 제공합니다. 수집, 정규화, 로컬 저장, 변경 감지, 그리고 작은 FastAPI 레퍼런스 API까지 포함합니다.

## 포함 내용

- Korea AIM NOTAM 엔드포인트 직접 수집
- 상위 소스가 불안정할 때를 위한 Selenium fallback
- 후속 자동화를 위한 정규화 JSON 레코드
- SQLite 저장 및 변경 감지 워크플로
- 자체 호스팅 가능한 FastAPI 레퍼런스 API
- 로컬 통합 검증용 샘플 fixture와 테스트

## 빠른 시작

### 1. 의존성 설치

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

### 2. 레퍼런스 API 실행

```bash
python3 -m uvicorn reference_api.main:app --reload
```

열어볼 주소:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/api/v1/notams`

### 3. 샘플 NOTAM 조회

```bash
curl "http://127.0.0.1:8000/api/v1/notams/RKSI"
```

예시 응답:

```json
{
  "location": "RKSI",
  "count": 1,
  "backend": "sample",
  "data": [
    {
      "notam_no": "A0001/26",
      "location": "RKSI",
      "qcode": "QMRLC",
      "is_active": true,
      "full_text": "RWY inspection in progress"
    }
  ]
}
```

## 이 저장소가 필요한 이유

한국 NOTAM 데이터 접근은 여전히 독립 개발자, 연구자, 소규모 제품팀에게 불편합니다. 이 프로젝트는 다른 팀이 항공 관련 워크플로를 더 빨리 만들 수 있도록, 반복되는 스크래핑, 파싱, 정규화 작업을 재사용 가능한 인프라 형태로 줄이기 위해 존재합니다.

## 이런 팀에 적합합니다

- 항공 연구 및 교육 프로젝트
- 비행계획 또는 디스패치 프로토타입
- 드론 및 UAM 브리핑 도구
- 공항 운영 대시보드
- 한국 항공 고시 정보를 자체 호스팅 스택에서 정규화해 쓰려는 팀

## 주요 진입점

- `notam_crawler_api.py`: 직접 수집 경로
- `notam_hybrid_crawler.py`: 직접 수집 + Selenium fallback
- `notam_monitor.py`: 반복 체크용 모니터링 워크플로
- `notam_change_detector.py`: 변경 감지 보조 로직
- `reference_api/main.py`: FastAPI 레퍼런스 구현
- `examples/sample_notams.json`: 로컬 테스트 및 데모용 fixture

## 프로젝트 상태

이 저장소는 잘 다듬어진 SDK라기보다, 실제로 조합해서 쓸 수 있는 인프라 소프트웨어에 가깝습니다.

- 직접 크롤러가 주 경로입니다
- Selenium 크롤러는 fallback 경로입니다
- 레퍼런스 API는 실용적인 통합 표면을 보여주기 위한 것입니다
- 호스팅형 또는 상용 서비스는 같은 오픈소스 코어 위에 별도로 올릴 수 있습니다

## 추가 실행 명령

직접 크롤러 실행:

```bash
python3 notam_crawler_api.py
```

하이브리드 크롤러 실행:

```bash
python3 -m pip install -r requirements-selenium.txt
python3 notam_hybrid_crawler.py
```

모니터링 워크플로 실행:

```bash
python3 notam_monitor.py
```

테스트 실행:

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pytest
```

## 문서

- [API Reference](docs/api.md)
- [Architecture](docs/architecture.md)
- [Ecosystem Impact](docs/ecosystem-impact.md)
- [Roadmap](docs/roadmap.md)
- [Source And Safety Notes](docs/source-and-safety.md)
- [Use Cases](docs/use-cases.md)
- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security](SECURITY.md)

## 호스팅형 서비스 방향

별도 호스팅 랜딩 페이지는 여기 있습니다.

- https://notam-api-landing.vercel.app/

호스팅 방향이 오픈소스 저장소를 대체하는 것은 아닙니다. 이 저장소의 핵심 가치는 수집기, 파서, 스키마, 자체 호스팅 가능한 빌딩 블록에 있습니다.

## 중요 안내

- 이 저장소는 공식 정부 API가 아닙니다
- 상위 소스 시스템과 응답 형식은 변경될 수 있습니다
- 수집된 NOTAM 데이터는 원본 소스의 이용 조건을 따를 수 있습니다
- 운영 비행 브리핑이나 안전 필수 의사결정의 유일한 데이터 소스로 사용하면 안 됩니다

## 기여

다음 영역의 기여를 환영합니다.

- 파서 정확도 개선
- API 계약 설계
- 문서화
- 테스트 보강
- 한국 항공 데이터 검증

이슈나 PR을 열기 전에 [Contributing](CONTRIBUTING.md), [Code of Conduct](CODE_OF_CONDUCT.md), [Source And Safety Notes](docs/source-and-safety.md)를 먼저 읽어주세요.

## 라이선스

MIT. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
