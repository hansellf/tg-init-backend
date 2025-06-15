from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
from pathlib import Path

app = FastAPI()

@app.get("/init-data")
async def get_init_data():
    data_path = Path(__file__).parent / "data" / "sticker_data.json"
    with open(data_path, "r") as f:
        return json.load(f)

@app.post("/validate-initdata")
async def validate_initdata(request: Request):
    try:
        body = await request.json()
        init_data = body.get("initData")

        if not init_data:
            return JSONResponse(status_code=400, content={"error": "initData is required"})

        # Echo the init data for now (or validate it if needed)
        return {"data": init_data}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
