from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

import os


def generate_report(data):

    os.makedirs("reports", exist_ok=True)

    pdf_path = "reports/RetailForecastReport.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    title = styles["Title"]
    title.alignment = TA_CENTER

    heading = styles["Heading2"]

    normal = styles["BodyText"]

    story = []

    # ===================================================
    # Title
    # ===================================================

    story.append(
        Paragraph(
            "Retail Demand Forecast Report",
            title
        )
    )

    story.append(Spacer(1,25))

    # ===================================================
    # Forecast Summary
    # ===================================================

    story.append(
        Paragraph(
            "Forecast Summary",
            heading
        )
    )

    summary = [

        ["Store", data["store"]],

        ["Forecast Date", data["date"]],

        ["Predicted Sales", f"Rs. {data['predicted_sales']:,.2f}"],

        ["Demand Level", data["demand_level"]]

    ]

    table = Table(summary, colWidths=[170,250])

    table.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),1,colors.grey),

        ("BACKGROUND",(0,0),(0,-1),colors.lightgrey),

        ("BOTTOMPADDING",(0,0),(-1,-1),8),

        ("FONTNAME",(0,0),(-1,-1),"Helvetica")

    ]))

    story.append(table)

    story.append(Spacer(1,20))

    # ===================================================
    # Business Recommendations
    # ===================================================

    story.append(
        Paragraph(
            "Business Recommendations",
            heading
        )
    )

    recommendations = [

        data["inventory_action"],

        data["staffing_action"],

        data["promotion_action"]

    ]

    for item in recommendations:

        story.append(

            Paragraph(
                f"• {item}",
                normal
            )

        )

    story.append(Spacer(1,20))

    # ===================================================
    # Model Performance
    # ===================================================

    story.append(
        Paragraph(
            "Model Performance",
            heading
        )
    )

    performance = [

        ["Model","XGBoost"],

        ["R² Score","0.921"],

        ["MAE","629.67"],

        ["RMSE","882.91"]

    ]

    perf_table = Table(performance,colWidths=[170,250])

    perf_table.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),1,colors.grey),

        ("BACKGROUND",(0,0),(0,-1),colors.lightgrey),

        ("BOTTOMPADDING",(0,0),(-1,-1),8)

    ]))

    story.append(perf_table)

    story.append(Spacer(1,20))

    # ===================================================
    # Feature Importance
    # ===================================================

    story.append(
        Paragraph(
            "Top Demand Drivers",
            heading
        )
    )

    features = [

        "Promotion",

        "Lag_7 Sales",

        "Rolling Mean (30 Days)",

        "Competition Distance",

        "Month"

    ]

    for i, feature in enumerate(features,1):

        story.append(

            Paragraph(
                f"{i}. {feature}",
                normal
            )

        )

    story.append(Spacer(1,20))

    # ===================================================
    # Conclusion
    # ===================================================

    story.append(
        Paragraph(
            "Executive Summary",
            heading
        )
    )

    summary_text = f"""
    The forecast predicts sales of <b>Rs. {data['predicted_sales']:,.2f}</b>
    for Store <b>{data['store']}</b>.
    Current demand is classified as
    <b>{data['demand_level']}</b>.
    Based on historical trends and the XGBoost forecasting model,
    the recommended actions are to
    <b>{data['inventory_action'].lower()}</b>,
    <b>{data['staffing_action'].lower()}</b>,
    and
    <b>{data['promotion_action'].lower()}</b>.
    """

    story.append(
        Paragraph(
            summary_text,
            normal
        )
    )

    doc.build(story)

    return pdf_path