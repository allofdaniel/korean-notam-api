# Korean NOTAM API and Crawler

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

[![CI](https://github.com/allofdaniel/korean-notam-api/actions/workflows/ci.yml/badge.svg)](https://github.com/allofdaniel/korean-notam-api/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

韓国のNOTAMデータを収集、正規化、監視し、セルフホストまで行えるオープンソースのPythonツール群です。

韓国には、開発者がそのまま使いやすい公開NOTAM APIが事実上ありません。このリポジトリは、下流チームが毎回作り直しがちな中核レイヤーをまとめて提供します。収集、正規化、ローカル保存、変更検知、そして小さなFastAPIリファレンスAPIを含みます。

## 含まれるもの

- Korea AIM NOTAMエンドポイントからの直接収集
- 上流ソースが不安定な場合のためのSeleniumフォールバック
- 下流の自動化に使いやすい正規化JSONレコード
- SQLite保存と変更検知ワークフロー
- セルフホスト可能なFastAPIリファレンスAPI
- ローカル統合確認用のサンプルfixtureとテスト

## クイックスタート

### 1. 依存関係をインストール

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

### 2. リファレンスAPIを起動

```bash
python3 -m uvicorn reference_api.main:app --reload
```

開くURL:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/api/v1/notams`

### 3. サンプルNOTAMを取得

```bash
curl "http://127.0.0.1:8000/api/v1/notams/RKSI"
```

レスポンス例:

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

## このリポジトリが必要な理由

韓国のNOTAMデータへのアクセスは、独立開発者、研究者、小規模プロダクトチームにとって今も扱いにくいままです。このプロジェクトは、他チームが航空ワークフローをより速く構築できるように、繰り返し発生するスクレイピング、パース、正規化作業を再利用可能なインフラとしてまとめるために存在します。

## 役立つ対象

- 航空研究や教育プロジェクト
- フライトプランニングやディスパッチの試作
- ドローンやUAMのブリーフィングツール
- 空港運用ダッシュボード
- 韓国の航空告示をセルフホスト環境で正規化して使いたいチーム

## 主な入口

- `notam_crawler_api.py`: 直接収集パス
- `notam_hybrid_crawler.py`: 直接収集 + Seleniumフォールバック
- `notam_monitor.py`: 定期確認向け監視ワークフロー
- `notam_change_detector.py`: 変更検知ヘルパー
- `reference_api/main.py`: FastAPIリファレンス実装
- `examples/sample_notams.json`: ローカルテストとデモ用fixture

## プロジェクト状況

これは洗練されたSDKというより、実運用で組み合わせて使うためのインフラソフトウェアです。

- 直接クローラが主経路です
- Seleniumクローラはフォールバック経路です
- リファレンスAPIは実用的な統合面を示すためのものです
- ホスト型または商用サービスは同じOSSコアの上に別途構築できます

## 追加コマンド

直接クローラを実行:

```bash
python3 notam_crawler_api.py
```

ハイブリッドクローラを実行:

```bash
python3 -m pip install -r requirements-selenium.txt
python3 notam_hybrid_crawler.py
```

監視ワークフローを実行:

```bash
python3 notam_monitor.py
```

テストを実行:

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pytest
```

## ドキュメント

- [API Reference](docs/api.md)
- [Architecture](docs/architecture.md)
- [Ecosystem Impact](docs/ecosystem-impact.md)
- [Roadmap](docs/roadmap.md)
- [Source And Safety Notes](docs/source-and-safety.md)
- [Use Cases](docs/use-cases.md)
- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security](SECURITY.md)

## ホスト型サービスの方向性

別のホスト型ランディングページはこちらです。

- https://notam-api-landing.vercel.app/

ホスト型の方向性は、このオープンソースリポジトリを置き換えるものではありません。OSSとしての価値は、コレクタ、パーサ、スキーマ、そしてセルフホスト可能なビルディングブロックにあります。

## 重要事項

- これは公式な政府APIではありません
- 上流ソースシステムや応答形式は変更される可能性があります
- 取得したNOTAMデータは元ソースの利用条件に従う場合があります
- 運航ブリーフィングや安全上重要な判断の唯一の情報源として使わないでください

## コントリビュート

次の領域での貢献を歓迎します。

- パーサ精度の改善
- API契約設計
- ドキュメント整備
- テスト強化
- 韓国航空データの検証

[Contributing](CONTRIBUTING.md)、[Code of Conduct](CODE_OF_CONDUCT.md)、[Source And Safety Notes](docs/source-and-safety.md)を読んでからIssueやPRを作成してください。

## ライセンス

MIT. 詳細は[LICENSE](LICENSE)を参照してください。
