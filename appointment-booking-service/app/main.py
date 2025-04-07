from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
import uvicorn
import webbrowser

from app.api.endpoints.bookingRoute import booking_router

app = FastAPI()

allowed_origins = settings.ALLOWED_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(booking_router)

if __name__ == "__main__":
    webbrowser.open("http://localhost:8003/docs")
    uvicorn.run(app, host="0.0.0.0", port=8003)