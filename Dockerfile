FROM nvidia/cuda:12.2.0-cudnn8-runtime-ubuntu22.04

# Install Python & tools
RUN apt-get update && apt-get install -y \
    python3.11 python3.11-venv python3.11-dev python3-pip git poppler-utils \
    ttf-mscorefonts-installer msttcorefonts fonts-crosextra-caladea fonts-crosextra-carlito gsfonts lcdf-typetools && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

WORKDIR /app
COPY ./app /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --find-links https://flashinfer.ai/whl/cu124/torch2.4/flashinfer/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
