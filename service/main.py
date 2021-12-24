from storage.storage import Managment
from fastapi import Request, FastAPI

app = FastAPI()
m = Managment(autocreate=True)


@app.post("/store")
async def store(request: Request):
    response = await request.json()
    payload = response['payload']
    try:
        m.payload = payload
        return {"status": "success"}
    except Exception as err:
        return {"status": str(err)}


@app.post("/read")
async def read():
    try:
        payload = m.read()
        return {"status": "success", "payload": str(payload)}
    except Exception as err:
        return {"status": str(err)}


@app.get("/clear")
async def clear():
    try:
        payload = m.clear()
        return {"status": "success"}
    except Exception as err:
        return {"status": str(err)}
