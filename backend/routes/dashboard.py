from fastapi import APIRouter, HTTPException

from backend.config import MODEL_ACCURACY
from backend.services.store_service import get_store_dataset, get_sales_by_store_type, get_promotion_impact
from backend.services.actual_predict_service import get_actual_prediction_data

router = APIRouter()

@router.get("/store-types")
def sales_by_store_type():

    data = get_sales_by_store_type()

    return data.to_dict(orient="records")

@router.get("/dashboard/{store}")
def get_dashboard(store: int):

    store_data = get_store_dataset(store)

    if store_data.empty:
        raise HTTPException(
            status_code=404,
            detail="Store not found"
        )

    latest = store_data.sort_values("Date").iloc[-1]

    return {
        "store": store,
        "store_type": latest["StoreType"],
        "average_sales": round(store_data["Sales"].mean(), 2),
        "max_sales": int(store_data["Sales"].max()),
        "min_sales": int(store_data["Sales"].min()),
        "forecast_accuracy": MODEL_ACCURACY,
        "total_records": len(store_data),
        "last_sale": int(latest["Sales"])
    }


@router.get("/forecast/{store}")
def get_forecast(store: int):
    df = get_actual_prediction_data(store)

    if df.empty:
        raise HTTPException(
            status_code=404,
            detail="not found"
        )
    return df[["Date", "Actual", "Predicted"]].to_dict(orient="records")


@router.get("/promotion-impact")
def promotion_impact():
    data = get_promotion_impact()

    return data

    