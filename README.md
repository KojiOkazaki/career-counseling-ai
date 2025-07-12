キャリアカウンセリング評価AI

概要

本アプリケーションは、キャリアカウンセリングの音声データをAIで分析・評価するツールです。MP3やM4Aなどの音声ファイルをアップロードすると、AIがセッション内容を文字起こしし、専門的な評価基準に基づいて具体的な改善点やアドバイスを生成します。

技術スタック

文字起こし：OpenAI Whisper

評価生成：GPT-4o

開発言語：Python 3.8以上

音声処理：FFmpeg

個人情報とプライバシー

本アプリケーションでは、分析のためにアップロードされた音声データを外部のOpenAI APIに送信します。

氏名、連絡先、企業名などの機密情報や個人を特定できる情報を含む音声はアップロードしないでください。

本ツールの利用は、上記に同意したものとみなされます。データの取り扱いには十分注意し、自己責任でご利用ください。

動作環境

Python 3.8以上

FFmpeg（音声フォーマット処理用）

インストールと設定

1. リポジトリのクローン

git clone https://github.com/あなたのユーザー名/career-counseling-ai.git
cd career-counseling-ai

2. Python仮想環境の構築（推奨）

# 仮想環境の作成
python3 -m venv venv

# macOS / Linux
a source venv/bin/activate

# Windows
venv\Scripts\activate

3. 依存パッケージのインストール

pip install -r requirements.txt

4. APIキーの設定

プロジェクトルートに .env ファイルを作成し、以下の内容を記述します。

OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

.env ファイルは .gitignore に登録されており、リポジトリには含まれません。

実行方法

python app.py

起動後、ターミナルに表示されるローカルURL（例：http://127.0.0.1:7860）をウェブブラウザで開き、音声ファイルをアップロードして評価結果を確認してください。

ライセンス

MIT License
