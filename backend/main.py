from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.home import router as home_router
from backend.routes.prediction import router as prediction_router
from backend.routes.history import router as history_router
from backend.routes.dashboard import router as dashboard_router
from backend.routes.report import router as report_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(home_router)
app.include_router(prediction_router)
app.include_router(history_router)
app.include_router(dashboard_router)
app.include_router(report_router)