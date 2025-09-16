from fastapi import FastAPI, UploadFile
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "/tmp/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/ingest")
async def ingest(file: UploadFile):
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    # In real pipeline, push job to Redis queue
    return {"status": "queued", "filename": file.filename}

@app.get("/status/{job_id}")
def status(job_id: int):
    # Dummy response
    return {
        "job_id": job_id,
        "status": "completed",
        "fields": {
            "Fund ID": "ABC123",
            "LP ID": "LP456",
            "Call Amount": "1,000,000",
            "Currency": "USD",
            "Call Date": "2025-09-16"
        }
    }
