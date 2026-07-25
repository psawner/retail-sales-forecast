async function initDashboard() {
    const prediction = JSON.parse(localStorage.getItem("prediction")) || {};

    document.getElementById("forecastValue").innerHTML =
        prediction.predicted_sales ? `₹${prediction.predicted_sales}` : "₹0";

    document.getElementById("demandValue").innerHTML =
        prediction.demand_level;

    document.getElementById("inventoryStatus").innerHTML =
        prediction.inventory_action;

    const ul =
        document.getElementById("recommendationList");

    ul.innerHTML = "";

    [
        prediction.inventory_action,
        prediction.staffing_action,
        prediction.promotion_action
    ].forEach(text => {

        const li = document.createElement("li");

        li.textContent = text;

        ul.appendChild(li);

    });


    const response = await fetch(
        `http://127.0.0.1:8000/history/${prediction.store}`
    );

    const history = await response.json();

    const labels =
        history.map(x => x.Date);

    const sales =
        history.map(x => x.Sales);

    // ----------------------
    // Monthly Sales Trend
    // ----------------------

    new Chart(
        document.getElementById("salesChart"),
        {

            type: "line",

            data: {

                labels: labels,

                datasets: [{

                    label: "Sales",

                    data: sales

                }]

            }

        });


    // ----------------------
    // Store Type Revenue
    // ----------------------

    const store_response =
        await fetch("http://127.0.0.1:8000/store-types");

    const data = await store_response.json();

    const store_labels =
        data.map(x => x.StoreType);

    const store_sales =
        data.map(x => x.Sales);

    new Chart(
        document.getElementById("storeChart"),
        {
            type: "bar",

            data: {
                labels: store_labels,

                datasets: [{
                    label: "Average Sales",

                    data: store_sales
                }]
            }
        }
    );


    // ----------------------
    // Actual vs Predicted
    // ----------------------

    const predict_response = await fetch(
        `http://127.0.0.1:8000/forecast/${prediction.store}`
    );

    const predict_data = await predict_response.json();

    const predict_dates = predict_data.map(x => x.Date);
    const predict_actual = predict_data.map(x => x.Actual);
    const predict_predicted = predict_data.map(x => x.Predicted);

    new Chart(document.getElementById("predictionChart"), {
        type: "line",
        data: {
            labels: predict_dates,
            datasets: [
                {
                    label: "Actual",
                    data: predict_actual
                },
                {
                    label: "Predicted",
                    data: predict_predicted
                }
            ]
        }
    });


    // ----------------------
    // Promotion Impact
    // ----------------------

    const promo_response = await fetch(
        "http://127.0.0.1:8000/promotion-impact"
    );

    const promo_data = await promo_response.json();

    new Chart(
        document.getElementById("promoChart"),
        {
            type: "bar",
            data: {
                labels: ["Without Promotion", "With Promotion"],
                datasets: [{
                    label: "Average Sales",
                    data: [
                        promo_data.average_sales_no_promo,
                        promo_data.average_sales_promo
                    ]
                }]
            }
        }
    );


    // ----------------------
    // Download Report
    // ----------------------

    document
        .getElementById("downloadBtn")
        .addEventListener("click", async () => {

            const prediction =
                JSON.parse(localStorage.getItem("prediction"));

            const response = await fetch(
                "http://127.0.0.1:8000/report",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify(prediction)
                }
            );

            const blob = await response.blob();

            const url = window.URL.createObjectURL(blob);

            const a = document.createElement("a");

            a.href = url;

            a.download = "RetailForecastReport.pdf";

            a.click();

            window.URL.revokeObjectURL(url);

        });
}

initDashboard();