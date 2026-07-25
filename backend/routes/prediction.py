from fastapi import APIRouter
from backend.model.schemas import SalesPredictForm
from backend.model.ml_model import model, feature_columns

from backend.services.feature_engineering import create_features
from backend.services.recommendation_eng import get_business_recommendations

import pandas as pd

router = APIRouter()


@router.post("/predict")
def predict(form: SalesPredictForm):
    data = pd.DataFrame([{
        "Store": form.store,
        "date": form.date,
        "promo": form.promo,
        "state_holiday": form.state_holiday,
        "school_holiday": form.school_holiday,
        "open": form.is_open
    }])

    data = create_features(data)

    data = data[feature_columns]

    # Predict
    prediction = float(model.predict(data)[0])

    rolling_mean = float(data["RollingMean_30"].iloc[0])

    recommendations = get_business_recommendations(
        predicted_sales=prediction,
        rolling_mean_30=rolling_mean,
        promo=form.promo
    )

    return {
        "store": form.store,
        "date": str(form.date),
        "predicted_sales": round(float(prediction), 2),
        **recommendations
    }

