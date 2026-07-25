from backend.services.store_service import store_metadata
from backend.services.lag_service import lag_features
import pandas as pd
import numpy as np


def create_features(data):

    # Convert date
    data["date"] = pd.to_datetime(data["date"])

    # Calendar features
    data["Year"] = data["date"].dt.year
    data["Month"] = data["date"].dt.month
    data["Quarter"] = data["date"].dt.quarter
    data["Week"] = data["date"].dt.isocalendar().week.astype(int)
    data["Day"] = data["date"].dt.day
    data["DayOfYear"] = data["date"].dt.dayofyear
    data["WeekOfYear"] = data["date"].dt.isocalendar().week.astype(int)

    # Day of week
    data["DayOfWeek"] = data["date"].dt.dayofweek + 1

    # Weekend
    data["IsWeekend"] = data["DayOfWeek"].isin([6,7]).astype(int)

    # Month boundaries
    data["IsMonthStart"] = data["date"].dt.is_month_start.astype(int)
    data["IsMonthEnd"] = data["date"].dt.is_month_end.astype(int)

    # Cyclical encoding
    data["Month_sin"] = np.sin(2*np.pi*data["Month"]/12)
    data["Month_cos"] = np.cos(2*np.pi*data["Month"]/12)

    data["DayOfWeek_sin"] = np.sin(2*np.pi*data["DayOfWeek"]/7)
    data["DayOfWeek_cos"] = np.cos(2*np.pi*data["DayOfWeek"]/7)

    data["Promo"] = data["promo"].astype(int)
    data["StateHoliday"] = data["state_holiday"].astype(int)
    data["SchoolHoliday"] = data["school_holiday"].astype(int)
    data["Open"] = data["open"].astype(int)

    data = store_metadata(data)
    data = lag_features(data)

    return data