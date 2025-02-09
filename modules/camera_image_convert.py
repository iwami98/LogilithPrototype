import cv2
import time
import os
import base64
from dotenv import load_dotenv

# .env ファイルを読み込む
load_dotenv()

def capture_image(filename="captured_image.jpg", camera_index=0):
    # カメラを開く
    cap = cv2.VideoCapture(camera_index)
    
    if not cap.isOpened():
        print("カメラを開けませんでした。")
        return None
    
    # カメラの準備
    time.sleep(2)  # カメラの自動調整のために待機
    
    # 画像をキャプチャ
    ret, frame = cap.read()
    
    if ret:
        # 保存ディレクトリを .env から取得
        save_dir = os.getenv("CAPTURE_DIRECTORY", "./capture")
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, filename)
        
        # 画像を保存
        cv2.imwrite(save_path, frame)
        print(f"画像を {save_path} に保存しました。")
        
        # 画像をbase64に変換
        _, buffer = cv2.imencode(".jpg", frame)
        img_base64 = base64.b64encode(buffer).decode("utf-8")
        
        # Base64を.txtに保存
        txt_path = os.path.join(save_dir, "captured_image_base64.txt")
        with open(txt_path, "w") as txt_file:
            txt_file.write(img_base64)
        print(f"Base64エンコードされた画像データを {txt_path} に保存しました。")
        
        return txt_path
    else:
        print("画像を取得できませんでした。")
        return None
    
    # カメラを解放
    cap.release()
    cv2.destroyAllWindows()
    
    if txt_path:
        print(f"Base64データが保存されたファイル: {txt_path}")
