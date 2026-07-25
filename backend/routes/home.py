from fastapi import APIRouter
import pandas as pd
from backend.model.ml_model import model, feature_columns
from backend.services.feature_engineering import create_features
from backend.services.recommendation_eng import get_business_recommendations

router = APIRouter()

@router.get("/home")
def home_dashboard():

    # Default store shown on landing page
    store = 1

    # Forecast for today
    today = pd.Timestamp.today().normalize()

    data = pd.DataFrame([{
        "Store": store,
        "date": today,
        "promo": False,
        "state_holiday": False,
        "school_holiday": False,
        "open": True
    }])

    data = create_features(data)

    data = data[feature_columns]

    prediction = float(model.predict(data)[0])

    rolling_mean = float(data["RollingMean_30"].iloc[0])

    recommendations = get_business_recommendations(
        prediction,
        rolling_mean,
        False
    )

    return {
        "today_forecast": round(prediction,2),
        "demand": recommendations["demand_level"],
        "change": recommendations["sales_change_percent"]
    }