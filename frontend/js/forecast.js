const form = document.getElementById("forecastForm");
const resultEl = document.getElementById("result");
const predictBtn = form.querySelector("button");
const mid = document.querySelector(".mid");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    predictBtn.disabled = true;
    predictBtn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Predicting...`;

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

    try{

        const response = await fetch(`${API}/predict`,{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(payload)

        });

        if(!response.ok){

            throw new Error("Unable to generate prediction.");

        }

        const data = await response.json();

        localStorage.setItem("prediction",JSON.stringify(data));

        showPrediction(data);

    }

    catch(error){

        resultEl.style.display="block";

        mid.classList.add("show-result");

        resultEl.innerHTML=`

        <div class="prediction-container">

            <h2>Prediction Failed</h2>

            <div class="metric">

                <span>Error</span>

                <strong>${error.message}</strong>

            </div>

        </div>

        `;

    }

    finally{

        predictBtn.disabled=false;

        predictBtn.innerHTML="Predict";

    }

});


function showPrediction(data){

    mid.classList.add("show-result");

    resultEl.style.display="block";

    const sales = Number(data.predicted_sales).toLocaleString("en-IN",{

        minimumFractionDigits:2,

        maximumFractionDigits:2

    });

    const demandColor = getDemandColor(data.demand_level);

    resultEl.innerHTML=`

    <div class="prediction-container">

        <h2>
            <i class="fa-solid fa-chart-line"></i>
            Forecast Result
        </h2>

        <div class="metric sales">

            <span>Predicted Sales</span>

            <strong>₹${sales}</strong>

        </div>

        <div class="metric demand">

            <span>Demand Level</span>

            <strong style="color:${demandColor}">
                ${data.demand_level}
            </strong>

        </div>

        <div class="metric change">

            <span>Expected Change</span>

            <strong>${data.sales_change_percent}%</strong>

        </div>

        <div class="metric inventory">

            <span>Inventory</span>

            <strong>${data.inventory_action}</strong>

        </div>

        <div class="metric staff">

            <span>Staffing</span>

            <strong>${data.staffing_action}</strong>

        </div>

        <div class="metric promotion">

            <span>Promotion</span>

            <strong>${data.promotion_action}</strong>

        </div>

    </div>

    `;

}



function getDemandColor(level){

    switch(level.toLowerCase()){

        case "high":
            return "#16a34a";

        case "medium":
            return "#f59e0b";

        case "low":
            return "#dc2626";

        default:
            return "#2563eb";

    }

}