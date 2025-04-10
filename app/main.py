from fastapi import FastAPI, UploadFile, File
from olmocr.ocr import OlmOCR
from PIL import Image
import io

app = FastAPI()
ocr = OlmOCR()

@app.post("/ocr/")
async def extract_text(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    result = ocr(image)
    return {"text": result}
