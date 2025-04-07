import uvicorn
from app.api.endPoint.server import application as app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8004)
