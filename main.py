import json
import re
import time
from modules import motor_control as moving
from modules import prompt_request as thinking
from modules import camera_image_convert as looking


def extract_json(text):
    # 正規表現でJSON部分を抽出
    json_pattern = re.findall(r'\{.*?\}|\[.*?\]', text, re.DOTALL)
    return json_pattern

if __name__ == "__main__":
    start_time = time.time()  # 開始時間を記録
    duration = 30 * 60  # 30分 (秒換算)

    while time.time() - start_time < duration:
        looking.capture_image()

        try:
            data = json.loads(thinking.llm_result())
            
            # 必要なキーが揃っているか確認
            if "command" in data and "speed" in data and "duration" in data:
                moving.move(data["command"], data["speed"], data["duration"])
            else:
                print("Invalid command format")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format")