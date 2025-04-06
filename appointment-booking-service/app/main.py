from fastapi import FastAPI, Depends
import uvicorn
import webbrowser

from app.api.endpoints.bookingRoute import booking_router

app = FastAPI()

app.include_router(booking_router)

if __name__ == "__main__":
    webbrowser.open("http://localhost:8003/docs")
    uvicorn.run(app, host="0.0.0.0", port=8003)