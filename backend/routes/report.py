from fastapi import APIRouter
from fastapi.responses import FileResponse
from backend.services.report_service import generate_report

router = APIRouter()

@router.post("/report")
def download_report(report_data: dict):

    pdf = generate_report(report_data)

    return FileResponse(
        pdf,
        media_type="application/pdf",
        filename="RetailForecastReport.pdf"
    )