import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
