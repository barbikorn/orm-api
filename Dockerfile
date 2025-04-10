FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y \
    python3.11 python3.11-venv python3.11-dev python3-pip git && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install runpod

# สำหรับ RunPod Serverless ไม่จำเป็นต้องเปิด uvicorn server
CMD ["python", "-u", "handler.py"]
