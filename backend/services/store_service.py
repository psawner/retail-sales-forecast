import pandas as pd
from backend.data_loader import load_csv


store_df = load_csv("data/processed/clean_sales.csv")

def store_metadata(data):
    store_df["PromoInterval"] = store_df["PromoInterval"].fillna("")

    store_info = store_df.loc[
        store_df["Store"] == data["Store"].iloc[0]
    ].iloc[0]

    promo_interval_map = {
            "": 0,
            "Jan,Apr,Jul,Oct": 1,
            "Feb,May,Aug,Nov": 2,
            "Mar,Jun,Sept,Dec": 3
    }
    
    data["PromoInterval"] = promo_interval_map.get(
        store_info["PromoInterval"],
        0
    )

    # Encode categorical
    store_type_map = {"a":0, "b":1, "c":2, "d":3}
    assortment_map = {"a":0, "b":1, "c":2}
        
    data["StoreType"] = store_type_map[store_info["StoreType"]]
    data["Assortment"] = assortment_map[store_info["Assortment"]]
    
    #Competition distance and promo
    
    data["CompetitionDistance"] = store_info["CompetitionDistance"]
    
    data["Promo2"] = store_info["Promo2"]

    data["Promo2SinceWeek"] = store_info["Promo2SinceWeek"]
    
    data["Promo2SinceYear"] = store_info["Promo2SinceYear"]
    
    data["CompetitionOpenSinceMonth"] = store_info["CompetitionOpenSinceMonth"]
    
    data["CompetitionOpenSinceYear"] = store_info["CompetitionOpenSinceYear"]
    
    comp_start = pd.Timestamp(
        year=int(store_info["CompetitionOpenSinceYear"]),
        month=int(store_info["CompetitionOpenSinceMonth"]),
        day=1
    )
    
    current = data["date"].iloc[0]
    
    data["CompetitionAgeMonths"] = max(
        0,
        (current.year - comp_start.year) * 12 +
        (current.month - comp_start.month)
    )

    if store_info["Promo2"] == 1:

        promo_start = pd.to_datetime(
            f"{int(store_info['Promo2SinceYear'])}-W{int(store_info['Promo2SinceWeek'])}-1",
            format="%Y-W%W-%w"
        )

        current = data["date"].iloc[0]

        data["PromoDurationMonths"] = max(
            0,
            (current.year - promo_start.year) * 12 +
            (current.month - promo_start.month)
        )

    else:

        data["PromoDurationMonths"] = 0

    return data

def get_store_data():
    return store_df


def get_sales_by_store_type():

    store_df = get_store_data()

    return (
        store_df
        .groupby("StoreType")["Sales"]
        .mean()
        .reset_index()
    )

def get_store_dataset(store: int):
    store_df = get_store_data()

    return (
        store_df[store_df["Store"] == store]
        .sort_values("Date")
        .copy()
    )


def get_promotion_impact():
    store_df = get_store_data()
    promo_sales = store_df.groupby("Promo")["Sales"].mean().reindex([0, 1])

    avg_sales_no_promo = float(promo_sales.loc[0]) if 0 in promo_sales.index else None
    avg_sales_promo = float(promo_sales.loc[1]) if 1 in promo_sales.index else None
    promotion_impact = (
        avg_sales_promo - avg_sales_no_promo
        if avg_sales_promo is not None and avg_sales_no_promo is not None
        else None
    )

    return {
        "average_sales_no_promo": round(avg_sales_no_promo, 2),
        "average_sales_promo": round(avg_sales_promo, 2),
        "promotion_impact": round(promotion_impact, 2),
        "promotion_lift_percent": round(
            ((avg_sales_promo - avg_sales_no_promo) / avg_sales_no_promo) * 100,
            2
        ),
        "recommendation": (
            "Continue promotions"
            if promotion_impact > 0
            else "Review promotion strategy"
        )
    }

