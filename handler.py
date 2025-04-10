import runpod
import io
from PIL import Image
import base64
from olmocr.ocr import OlmOCR

# โหลดโมเดลเมื่อ container เริ่มทำงาน (เพื่อลดเวลา cold start)
ocr = OlmOCR()

def handler(event):
    # วิธีรับข้อมูลจาก RunPod
    try:
        if "image" not in event["input"]:
            return {"error": "No image provided"}
        
        # กรณีส่งเป็น base64
        if event["input"].get("isBase64", False):
            image_data = base64.b64decode(event["input"]["image"])
            image = Image.open(io.BytesIO(image_data))
        # กรณีส่ง URL
        elif event["input"]["image"].startswith(("http://", "https://")):
            import requests
            response = requests.get(event["input"]["image"])
            image = Image.open(io.BytesIO(response.content))
        else:
            return {"error": "Invalid image format"}
        
        # ส่งไปยัง OCR model
        result = ocr(image)
        
        return {"text": result}
    
    except Exception as e:
        return {"error": str(e)}

# แปลง handler function ให้กลายเป็น RunPod endpoint
runpod.serverless.start({"handler": handler}) 