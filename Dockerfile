FROM python:3.10-alpine3.18

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
EXPOSE 80
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
