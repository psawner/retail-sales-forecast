def get_business_recommendations(
    predicted_sales: float,
    rolling_mean_30: float,
    promo: bool
):
    predicted_sales = float(predicted_sales)
    rolling_mean_30 = float(rolling_mean_30)
    recommendations = {}

    # -----------------------------
    # Demand Level
    # -----------------------------
    change = float(((predicted_sales - rolling_mean_30) / rolling_mean_30) * 100)

    if change >= 20:
        demand = "High"
    elif change <= -20:
        demand = "Low"
    else:
        demand = "Normal"

    recommendations["demand_level"] = demand
    recommendations["sales_change_percent"] = float(round(change, 2))

    # -----------------------------
    # Inventory Recommendation
    # -----------------------------
    if change >= 20:
        recommendations["inventory_action"] = (
            "Increase inventory to avoid stockouts."
        )

    elif change <= -20:
        recommendations["inventory_action"] = (
            "Reduce replenishment to minimize overstock."
        )

    else:
        recommendations["inventory_action"] = (
            "Maintain current inventory level."
        )

    # -----------------------------
    # Staffing Recommendation
    # -----------------------------
    if demand == "High":
        recommendations["staffing_action"] = (
            "Schedule additional staff during peak hours."
        )

    elif demand == "Low":
        recommendations["staffing_action"] = (
            "Normal staffing is sufficient."
        )

    else:
        recommendations["staffing_action"] = (
            "Maintain regular staffing schedule."
        )

    # -----------------------------
    # Promotion Recommendation
    # -----------------------------
    if not promo and demand == "Low":
        recommendations["promotion_action"] = (
            "Consider launching a promotion to boost demand."
        )

    elif promo and demand == "High":
        recommendations["promotion_action"] = (
            "Current promotion is performing well."
        )

    elif promo and demand == "Low":
        recommendations["promotion_action"] = (
            "Review promotion strategy; current campaign has limited impact."
        )

    else:
        recommendations["promotion_action"] = (
            "No promotion changes recommended."
        )

    return recommendations