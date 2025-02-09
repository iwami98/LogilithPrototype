# README

## プロジェクト概要
このプロジェクトは、カメラで画像をキャプチャし、その画像データを使用してLLM（大規模言語モデル）に解析を依頼し、取得したコマンドを基にモーターを制御するシステムです。Raspberry Pi上で動作することを想定しています。まだ開発段階のプロトタイプです。

## 実行環境
- ハードウェア: Raspberry Pi 4 (4GB RAM)
- ソフトウェア: Python 3.12.4

## 構成ファイル

### `main.py`
メインのスクリプトで、以下の処理を実行します。
1. カメラで画像をキャプチャする。
2. LLMに画像データを送信し、制御コマンドを取得する。
3. コマンドを解析し、モーターを適切に動作させる。

### `camera_image_convert.py`
カメラを制御し、画像をキャプチャして保存し、さらにBase64形式に変換するモジュールです。
- OpenCVを使用して画像を取得。
- 画像を指定のディレクトリに保存。
- 画像をBase64エンコードし、テキストファイルとして保存。

### `motor_control.py`
Raspberry PiのGPIOを制御し、モーターを動作させるモジュールです。
- `forward`（前進）
- `backward`（後退）
- `left`（左旋回）
- `right`（右旋回）
- `stop`（停止）

### `prompt_request.py`
LLMと通信し、適切なコマンドを取得するモジュールです。
- `.env` からAPI設定を読み込む。
- キャプチャした画像のBase64データを含め、LLMにリクエストを送信。
- 取得した応答をJSONとして解析。

## 依存ライブラリ
本プロジェクトは以下のライブラリを使用します。

```
pip install -r requirements.txt
```

## 実行方法
1. `.env` ファイルを作成し、以下の設定を記入してください。
   ```
    CAPTURE_DIRECTORY="./capture"
    MODEL_NAME="llama3.2-vision:11b"
    SYSTEM_PROMPT="あなたは2輪のDCモータと1080pカメラを搭載したロボットの、頭脳であるAPIです。必ずJSONの返答をしてください"
    IMAGE_BASE64_PATH=${CAPTURE_DIRECTORY}/captured_image_base64.txt
    OLLAMA_HOST="<Ollama_Server_IP>"
    PROMPT_PATH="./main_prompt.md"
   ```
2. スクリプトを実行します。
   ```
   python3 main.py
   ```

## 注意事項
- Raspberry Piで実行する場合、GPIO制御のために `RPi.GPIO` ライブラリが必要です。
- カメラモジュールを使用するため、Raspberry Piの設定でカメラを有効化してください。
- `.env` ファイルのパス設定を適切に行ってください。
- モーターの接続と電源供給を正しく行ってください。

