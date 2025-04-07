from fastapi import FastAPI, Depends
import uvicorn
import webbrowser
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings

from app.api.endpoints.userRoutes import user_router

app = FastAPI()

allowed_origins = settings.ALLOWED_ORIGINS


app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)

if __name__ == "__main__":
    webbrowser.open("http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)