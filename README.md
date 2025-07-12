# キャリアカウンセリング評価AI

## 概要
AIがキャリアカウンセリング音声を文字起こし・評価し、改善点を提示するツール

## 技術スタック
- **文字起こし**：OpenAI Whisper
- **評価生成**：GPT-4o
- **言語**：Python 3.8+
- **音声処理**：FFmpeg

## プライバシー
- 音声データはOpenAI APIに送信されます
- 氏名・連絡先など個人情報は含めないでください

## 動作環境
- Python 3.8+
- FFmpeg（必須）

## インストール
以下のコマンドを順に実行してください。

    git clone https://github.com/あなたのユーザー名/career-counseling-ai.git
    cd career-counseling-ai
    python3 -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt

## 設定
プロジェクトルートに **.env** ファイルを作成し、以下を記述してください。

    OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

## 実行
以下のコマンドでアプリケーションを起動します。

    python app.py

起動後、ターミナルに表示されるURL（例：http://127.0.0.1:7860）をブラウザで開き、音声ファイルをアップロードして評価結果を確認してください。

## ライセンス
MIT License
