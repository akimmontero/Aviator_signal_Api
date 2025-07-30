
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/signal")
def get_signal():
    return {
        "signal": "3x45",
        "updated_at": datetime.now().strftime("%H:%M:%S")
      
