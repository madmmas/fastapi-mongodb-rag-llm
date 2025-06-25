from fastapi import FastAPI

app = FastAPI()


@app.get("/heartbeat")
async def heartbeat():
    return {"status": "ok"}
