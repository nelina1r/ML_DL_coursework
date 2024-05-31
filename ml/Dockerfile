FROM python:3.11-slim-bullseye

RUN rm -rf /usr/local/cuda/lib64/stubs

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git

WORKDIR /app

# Ensure requirements.txt is at the root of the build context
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt --extra-index-url https://download.pytorch.org/whl/cu121

RUN useradd -m huggingface

USER huggingface

ENV USE_TORCH=1
ENV PYTHONPATH=/app

CMD ["python", "/app/app/main.py"]
