from uuid import uuid4

import uvicorn
from fastapi import FastAPI
import lancedb


db_uri = "./test.lancedb"

app = FastAPI()
app.state.instance_id = str(uuid4())
app.state.db = lancedb.connect(db_uri)


@app.get("/")
def hello():
    return {"message": "Hello World!"}


@app.get("/id")
def instance_id():
    return {"instance_id": app.state.instance_id}


@app.get("/data")
def get_all_tables():
    table_names = [table_name for table_name in app.state.db.table_names()]
    return {"instance_id": app.state.instance_id, "message": f"Tables: {table_names}"}


@app.post("/data")
def insert_data(table_name: str):
    table = app.state.db.create_table(
        table_name,
        data=[
            {"vector": [3.1, 4.1], "item": "foo", "price": 10.0},
            {"vector": [5.9, 26.5], "item": "bar", "price": 20.0}
        ]
    )
    print(table)
    return {"instance_id": app.state.instance_id, "message": f"Table {table_name} was created."}


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=80, log_level="info")
    server = uvicorn.Server(config)
    server.run()
