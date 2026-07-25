const counters = document.querySelectorAll(".counter");

const observer = new IntersectionObserver(entries => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            const counter = entry.target;

            const target = +counter.dataset.target;

            let count = 0;

            const step = target / 120;

            const update = () => {

                count += step;

                if (count < target) {

                    counter.innerText = Math.floor(count);

                    requestAnimationFrame(update);

                }
                else {

                    counter.innerText = target.toLocaleString();

                }

            }

            update();

            observer.unobserve(counter);

        }

    })

});

const infoToggle = document.getElementById('infoToggle');
const techSection = document.getElementById('tech');
const closeTech = document.getElementById('closeTech');

function toggleTech(event) {
    event.preventDefault();
    const isVisible = techSection.classList.toggle('visible');
    techSection.classList.toggle('hidden', !isVisible);
    const icon = infoToggle.querySelector('i');
    icon.className = isVisible ? 'fa-solid fa-xmark' : 'fa-solid fa-info';
}

infoToggle.addEventListener('click', toggleTech);
closeTech.addEventListener('click', function (event) {
    event.preventDefault();
    techSection.classList.add('hidden');
    techSection.classList.remove('visible');
    const icon = infoToggle.querySelector('i');
    icon.className = 'fa-solid fa-info';
});


counters.forEach(counter => observer.observe(counter));

window.onload = async () => {

    const response = await fetch(
        "http://127.0.0.1:8000/home"
    );

    const data = await response.json();

    document.getElementById("forecast").innerText =
        "₹ " + data.today_forecast;

    document.getElementById("demand").innerText =
        data.demand;

    document.getElementById("change").innerText =
        data.change + "%";
}