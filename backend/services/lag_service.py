import pandas as pd

sales_history = pd.read_csv(r"data/processed/feature_engineered_data.csv")

def lag_features(data):
    sales_history["Date"] = pd.to_datetime(sales_history["Date"])

    history = (
        sales_history[sales_history["Store"] == data["Store"].iloc[0]]
        .sort_values("Date")
    )

    current_date = data["date"].iloc[0]
    
    history = history[
        history["Date"] < current_date
    ]

    data["Lag_1"] = history.iloc[-1]["Sales"]
    data["Lag_7"] = history.iloc[-7]["Sales"]
    data["Lag_14"] = history.iloc[-14]["Sales"]

    if len(history) >= 30:
        data["Lag_30"] = history.iloc[-30]["Sales"]
    else:
        data["Lag_30"] = history.iloc[0]["Sales"]       

    data["RollingMean_7"] = history.tail(7)["Sales"].mean()
    data["RollingMean_14"] = history.tail(14)["Sales"].mean()
    data["RollingMean_30"] = history.tail(30)["Sales"].mean()
    data["RollingStd_7"] = history.tail(7)["Sales"].std()

    return data    

def get_sales_data():
    return sales_history


def get_store_history(store: int):
    sales_history = get_sales_data()

    return (
        sales_history[sales_history["Store"] == store]
        .sort_values("Date")
    )
    