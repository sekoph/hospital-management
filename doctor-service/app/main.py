from fastapi import FastAPI, Depends
import uvicorn
import webbrowser

from api.endpoints.doctorSpecializationRoute import doctor_specalization_router
from api.endpoints.doctorRoute import docter_router

app = FastAPI()


app.include_router(doctor_specalization_router)
app.include_router(docter_router)

if __name__ == "__main__":
    webbrowser.open("http://localhost:8002/docs")
    uvicorn.run(app, host="0.0.0.0", port=8002)