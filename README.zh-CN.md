# Korean NOTAM API and Crawler

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

[![CI](https://github.com/allofdaniel/korean-notam-api/actions/workflows/ci.yml/badge.svg)](https://github.com/allofdaniel/korean-notam-api/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

这是一个用于采集、标准化、监控并可自托管韩国NOTAM数据的开源Python工具集。

韩国目前实际上并没有一个开发者可以直接方便使用的公开NOTAM API。这个仓库把下游团队反复重建的核心层打包出来，包含采集、标准化、本地存储、变更检测，以及一个小型FastAPI参考API。

## 包含内容

- 直接采集 Korea AIM NOTAM 端点
- 当上游流程脆弱时可使用 Selenium 回退方案
- 便于下游自动化处理的标准化 JSON 记录
- SQLite 存储与变更检测工作流
- 可自托管的 FastAPI 参考 API
- 用于本地集成验证的示例 fixture 与测试

## 快速开始

### 1. 安装依赖

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

### 2. 启动参考 API

```bash
python3 -m uvicorn reference_api.main:app --reload
```

打开以下地址:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/api/v1/notams`

### 3. 查询示例 NOTAM 数据

```bash
curl "http://127.0.0.1:8000/api/v1/notams/RKSI"
```

示例响应:

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

## 为什么需要这个仓库

韩国 NOTAM 数据的获取对独立开发者、研究人员和小型产品团队来说仍然不方便。这个项目的目标是把重复出现的抓取、解析和标准化工作收敛为可复用的基础设施，让其他团队可以更快地构建航空相关工作流。

## 适合哪些团队

- 航空研究与教育项目
- 飞行计划或签派原型
- 无人机与 UAM 简报工具
- 机场运营仪表盘
- 需要在自托管栈中使用标准化韩国航空通告数据的团队

## 主要入口

- `notam_crawler_api.py`: 直接采集路径
- `notam_hybrid_crawler.py`: 直接采集 + Selenium 回退
- `notam_monitor.py`: 重复检查的监控工作流
- `notam_change_detector.py`: 变更检测辅助逻辑
- `reference_api/main.py`: FastAPI 参考实现
- `examples/sample_notams.json`: 本地测试与演示用 fixture

## 项目状态

这更像是可实际组合使用的基础设施软件，而不是一个打磨完整的 SDK。

- 直接爬虫是主路径
- Selenium 爬虫是回退路径
- 参考 API 用于展示一个实用的集成接口
- 托管型或商业服务可以建立在同一个开源核心之上

## 其他命令

运行直接爬虫:

```bash
python3 notam_crawler_api.py
```

运行混合爬虫:

```bash
python3 -m pip install -r requirements-selenium.txt
python3 notam_hybrid_crawler.py
```

运行监控工作流:

```bash
python3 notam_monitor.py
```

运行测试:

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pytest
```

## 文档

- [API Reference](docs/api.md)
- [Architecture](docs/architecture.md)
- [Ecosystem Impact](docs/ecosystem-impact.md)
- [Roadmap](docs/roadmap.md)
- [Source And Safety Notes](docs/source-and-safety.md)
- [Use Cases](docs/use-cases.md)
- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security](SECURITY.md)

## 托管服务方向

另一个托管落地页在这里:

- https://notam-api-landing.vercel.app/

托管方向并不取代这个开源仓库。这个仓库的核心价值在于采集器、解析器、模式以及可自托管的构建模块。

## 重要说明

- 这不是官方政府 API
- 上游源系统和响应格式可能发生变化
- 抓取到的 NOTAM 数据可能仍然受原始数据源条款约束
- 不要把这个仓库作为运行飞行简报或安全关键决策的唯一数据来源

## 贡献

欢迎围绕以下方向贡献:

- 提升解析精度
- API 契约设计
- 文档完善
- 加强测试
- 韩国航空数据验证

在提交 issue 或 PR 之前，请先阅读 [Contributing](CONTRIBUTING.md)、[Code of Conduct](CODE_OF_CONDUCT.md) 和 [Source And Safety Notes](docs/source-and-safety.md)。

## 许可证

MIT. 详见 [LICENSE](LICENSE)。
