from fastapi import FastAPI, Depends
import uvicorn
import webbrowser
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints.userRoutes import user_router

app = FastAPI()

origin = [
    "http://patient-hospital:8001",
    "http://localhost:8002",
    "http://localhost:8003",
    "http://localhost:8004",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)

if __name__ == "__main__":
    webbrowser.open("http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)