//  .menu-toggle {
  const toggleButton = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');
  toggleButton.addEventListener('click', () => {
    navLinks.classList.toggle('show');
  });


// Show Django messages as toasts
document.addEventListener("DOMContentLoaded", function() {
    const messageContainer = document.getElementById("django-messages");
    if (messageContainer) {
        const messages = messageContainer.getElementsByClassName("message");
        for (let msg of messages) {
            showToast(msg.textContent);
        }
    }
});

// Testimonial slider functionality
document.addEventListener("DOMContentLoaded", function () {
  const slider = document.querySelector(".testimonial-slider");
  const cards = document.querySelectorAll(".testimonial-card");
  let index = 0;
  const visibleCards = 3; // Show 3 at a time

  function showNextTestimonial() {
    index++;
    if (index > cards.length - visibleCards) {
      index = 0; // reset when reaching the end
    }
    slider.style.transform = `translateX(-${index * (100 / visibleCards)}%)`;
  }

  // Auto-slide every 4 seconds
  setInterval(showNextTestimonial, 4000);
});

// Team slider functionality
document.addEventListener("DOMContentLoaded", function () {
  const teamSlider = document.querySelector(".team-slider");
  const teamCards = document.querySelectorAll(".team-card");
  let teamIndex = 0;
  const visibleCards = 3; // Show 3 at a time

  function showNextTeam() {
    teamIndex++;
    if (teamIndex > teamCards.length - visibleCards) {
      teamIndex = 0; // reset when reaching the end
    }
    teamSlider.style.transform = `translateX(-${teamIndex * (100 / visibleCards)}%)`;
  }

  // Auto-slide every 4 seconds
  setInterval(showNextTeam, 4000);
});

function showToast(message) {
    const toast = document.createElement("div");
    toast.className = "toast";
    toast.textContent = message;
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.classList.add("show");
    }, 100);
    setTimeout(() => {
        toast.classList.remove("show");
        setTimeout(() => document.body.removeChild(toast), 500);
    }, 4000);
}

 function goToStep(step) {
    document.getElementById("step1").style.display = step === 1 ? "block" : "none";
    document.getElementById("step2").style.display = step === 2 ? "block" : "none";
  }

document.addEventListener("DOMContentLoaded", function () {
    const select = document.getElementById("country_code"); // match the form field ID
    if (!select) {
        console.error("Country code select element not found!");
        return;
    }

    fetch("/static/js/countries.json")
        .then(response => response.json())
        .then(data => {
            Object.keys(data).forEach(key => {
                const option = document.createElement("option");
                option.value = data[key]; // the code
                option.textContent = `${key} (${data[key]})`;
                select.appendChild(option);
            });

            // Initialize Select2
            $('#country_code').select2({
                placeholder: "Select country code",
                allowClear: true
            });
        })
        .catch(err => console.error("Error loading country codes:", err));
});