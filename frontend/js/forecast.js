const form = document.getElementById("forecastForm");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const payload = {

        store: Number(document.getElementById("store").value),

        date: document.getElementById("date").value,

        promo: document.getElementById("promo").value === "true",

        state_holiday:
            document.getElementById("stateHoliday").value === "true",

        school_holiday:
            document.getElementById("schoolHoliday").value === "true",

        is_open:
            document.getElementById("open").value === "true"

    };

    const response = await fetch(`${API}/predict`, {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(payload)

    });

    const data = await response.json();

    localStorage.setItem(
        "prediction",
        JSON.stringify(data)
    );

    const containerEl = document.querySelector(".container");
    const resultEl = document.getElementById("result");

    if (containerEl) containerEl.style.display = "block";
    if (resultEl) {
        resultEl.style.display = "block";
        resultEl.style.opacity = "0";
        resultEl.style.transform = "translateY(20px)";
        resultEl.style.transition = "opacity 250ms ease-out, transform 250ms ease-out";
        resultEl.innerHTML = `
<div class="prediction-container">
    <h2>Prediction</h2>
    <p><b>Predicted Sales:</b> ₹${data.predicted_sales}</p>
    <p><b>Demand Level:</b> ${data.demand_level}</p>
    <p><b>Expected Change:</b> ${data.sales_change_percent}%</p>
    <p><b>Inventory:</b> ${data.inventory_action}</p>
    <p><b>Staffing:</b> ${data.staffing_action}</p>
    <p><b>Promotion:</b> ${data.promotion_action}</p>
</div>
`;
        requestAnimationFrame(() => {
            resultEl.style.opacity = "1";
            resultEl.style.transform = "translateY(0)";
        });
        resultEl.scrollIntoView({ behavior: "smooth", block: "center" });
    }

});