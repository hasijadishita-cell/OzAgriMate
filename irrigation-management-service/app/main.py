from fastapi import FastAPI

app = FastAPI(title="OzAgriMate Irrigation Management Service")

@app.get("/health")
def health():
    return {"status": "ok"}