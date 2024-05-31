FROM python:3.11-slim

COPY ./app /app/app
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/main.py"]
