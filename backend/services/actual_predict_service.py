import pandas as pd
from backend.data_loader import load_csv


predict_actual  = load_csv("reports/actual_predictions.csv")

def get_prediction_data():
    return predict_actual

def get_actual_prediction_data(store: int):
    predict_df = get_prediction_data()

    return(
        predict_df[predict_df["Store"] == store]
            .sort_values("Date")
            .copy()
    )
