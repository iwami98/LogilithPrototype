import os
import requests
from dotenv import load_dotenv

# .env ファイルを読み込む
load_dotenv()

def llm_result():
    # .env から変数を取得
    OLLAMA_HOST = os.getenv("OLLAMA_HOST")
    MODEL_NAME = os.getenv("MODEL_NAME")
    # PROMPT = os.getenv("PROMPT")
    IMAGE_BASE64_PATH = os.getenv("IMAGE_BASE64_PATH")
    PROMPT_PATH = os.getenv("PROMPT_PATH")

    # TXTファイルの中身を読み込む
    if IMAGE_BASE64_PATH and os.path.exists(IMAGE_BASE64_PATH):
        with open(IMAGE_BASE64_PATH, "r", encoding="utf-8") as file:
            IMAGE_DATA = file.read().strip()
    else:
        IMAGE_DATA = ""

    # .mdファイルの読み込み
    with open(PROMPT_PATH, "r", encoding="utf-8") as file:
        prompt_content = file.read()

    # APIのエンドポイント
    url = f"http://{OLLAMA_HOST}:11434/api/generate"

    # リクエストのペイロード
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt_content,
        "stream": False,
        "images": [IMAGE_DATA]
    }

    # POSTリクエストを送信
    response = requests.post(url, json=payload)

    # レスポンスを出力
    response_data = response.json()
    if "response" in response_data:
        print("Response:", response_data["response"])
    return response_data["response"]