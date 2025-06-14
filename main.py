from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

@app.get("/init-data")
async def get_init_data():
    data_path = Path(__file__).parent / "data" / "sticker_data.json"
    with open(data_path, "r") as f:
        return json.load(f)