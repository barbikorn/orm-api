FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y \
    python3.11 python3.11-venv python3.11-dev python3-pip git && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

WORKDIR /app
COPY ./app /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --find-links https://flashinfer.ai/whl/cu121/torch2.1/flashinfer/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
