
const theme = {
    navy: "#131b3a",
    navySoft: "#232b4d",
    amber: "#ff7a29",
    amberSoft: "rgba(255, 122, 41, 0.15)",
    navyFill: "rgba(19, 27, 58, 0.06)",
    line: "#e3e6f0",
    muted: "#6b7590",
    grey: "#c9cfe0"
};

Chart.defaults.font.family = "'Inter', sans-serif";
Chart.defaults.color = theme.muted;
Chart.defaults.plugins.legend.labels.usePointStyle = true;
Chart.defaults.plugins.legend.labels.boxWidth = 8;

const baseScales = {
    x: {
        grid: { color: theme.line, drawTicks: false },
        border: { display: false }
    },
    y: {
        grid: { color: theme.line, drawTicks: false },
        border: { display: false }
    }
};

const lineChartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    layout: {
        padding: {
            bottom: 10
        }
    },
    plugins: {
        legend: { display: false }
    },
    scales: {
        ...baseScales,
        x: {
            ...baseScales.x,
            ticks: {
                autoSkip: true,
                maxTicksLimit: 8,
                maxRotation: 45,
                minRotation: 45
            }
        }
    }
};

async function initDashboard() {
    const prediction = JSON.parse(localStorage.getItem("prediction")) || {};

    const today = new Date().toISOString().split('T')[0];
    const formattedDate = prediction.date === today ? "Today's Forecast" : 
        new Date(prediction.date).toLocaleDateString('en-GB', { 
            day: '2-digit', 
            month: '2-digit', 
            year: 'numeric' 
        }).replace(/\//g, '-');

    document.getElementById("forecast_time").innerHTML =
        prediction.date ? formattedDate : "Today's Forecast";

    document.getElementById("store_no").innerHTML =
        prediction.store ? `Store No: ${prediction.store}` : "Store No: N/A";

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
        `${API}/history/${prediction.store}`
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

                    data: sales,

                    borderColor: theme.navy,
                    backgroundColor: theme.navyFill,
                    pointBackgroundColor: theme.amber,
                    pointBorderColor: theme.amber,
                    pointRadius: 3,
                    pointHoverRadius: 5,
                    tension: 0.35,
                    fill: true,
                    borderWidth: 2

                }]

            },
            options: lineChartOptions

        });


    // ----------------------
    // Store Type Revenue
    // ----------------------

    const store_response =
        await fetch(`${API}/store-types`);

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

                    data: store_sales,

                    backgroundColor: theme.navy,
                    hoverBackgroundColor: theme.amber,
                    borderRadius: 6,
                    maxBarThickness: 42
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: {
                    ...baseScales,
                    x: { ...baseScales.x, grid: { display: false } }
                }
            }
        }
    );

    const predict_response = await fetch(
        `${API}/forecast/${prediction.store}`
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
                    data: predict_actual,
                    borderColor: theme.navy,
                    backgroundColor: theme.navy,
                    pointRadius: 2,
                    tension: 0.3,
                    borderWidth: 2
                },
                {
                    label: "Predicted",
                    data: predict_predicted,
                    borderColor: theme.amber,
                    backgroundColor: theme.amber,
                    borderDash: [6, 4],
                    pointRadius: 2,
                    tension: 0.3,
                    borderWidth: 2
                }
            ]
        },
        options: {
            ...lineChartOptions,
            plugins: { legend: { display: true, position: "bottom" } }
        }

    });


    const promo_response = await fetch(
        `${API}/promotion-impact`
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
                    ],
                    backgroundColor: [theme.grey, theme.amber],
                    borderRadius: 6,
                    maxBarThickness: 60
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: "y",
                plugins: { legend: { display: false } },
                scales: {
                    ...baseScales,
                    y: { ...baseScales.y, grid: { display: false } }
                }
            }
        }
    );

    document
        .getElementById("downloadBtn")
        .addEventListener("click", async () => {

            const prediction =
                JSON.parse(localStorage.getItem("prediction"));

            const response = await fetch(
                `${API}/report`,
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