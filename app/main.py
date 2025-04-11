from fastapi import FastAPI, File, UploadFile
from olmocr.ocr import OlmOCR
from PIL import Image
import io
import os

ocr = OlmOCR()
app = FastAPI()

@app.post("/ocr/")
async def run_ocr(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename)[-1].lower()
    contents = await file.read()

    # Use PIL for images
    if ext in ['.png', '.jpg', '.jpeg']:
        image = Image.open(io.BytesIO(contents))
        result = ocr(image)
        return {"text": result}

    # TODO: You can expand this to convert PDF -> image if needed
    return {"error": "Only PNG, JPG supported for now."}
