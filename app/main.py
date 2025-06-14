
from fastapi import FastAPI, Request, HTTPException, Query
from app.utils import validate_init_data
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/init-data")
async def get_init_data(
    initData: str = Query(...),
    ton_amount: float = Query(...),
    wallet: str = Query(...),
    description: str = Query(...)
):
    try:
        data = validate_init_data(initData)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return JSONResponse({
        "user_id": data.get("user", {}).get("id"),
        "username": data.get("user", {}).get("username"),
        "ton_amount": ton_amount,
        "wallet": wallet,
        "description": description
    })
