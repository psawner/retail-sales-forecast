from fastapi import APIRouter, HTTPException
from backend.services.lag_service import get_store_history

router = APIRouter()
@router.get("/history/{store}")
def get_history(store: int):

    history = get_store_history(store)

    if history.empty:
        raise HTTPException(status_code=404, detail="Store not found")

    history = history.tail(30)
    history["Date"] = history["Date"].astype(str)

    return history[["Date", "Sales"]].to_dict("records")