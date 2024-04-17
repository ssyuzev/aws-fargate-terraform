FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
EXPOSE 80
RUN pip install -U pip && pip install -r requirements.txt --no-cache-dir

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
