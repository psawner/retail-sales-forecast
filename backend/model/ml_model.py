import joblib

model = joblib.load("./artifacts/xgboost_sales_forecast.pkl")
feature_columns = joblib.load("./artifacts/features.pkl")