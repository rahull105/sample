// CATEGORY TABS FILTER
const tabs = document.querySelectorAll(".tab");
const cards = document.querySelectorAll(".card");
const indicator = document.querySelector(".tab-indicator");

tabs.forEach((tab, i) => {
  tab.addEventListener("click", () => {
    tabs.forEach((t) => t.classList.remove("active"));
    tab.classList.add("active");

    indicator.style.width = tab.offsetWidth + "px";
    indicator.style.left = tab.offsetLeft + "px";

    const cat = tab.dataset.category;
    cards.forEach((card) => {
      card.style.display =
        cat === "all" || card.dataset.category === cat ? "block" : "none";
    });
  });
});

// 3D CARD TILT
document.querySelectorAll(".tilt").forEach((card) => {
  card.addEventListener("mousemove", (e) => {
    const r = card.getBoundingClientRect();
    const x = e.clientX - r.left;
    const y = e.clientY - r.top;
    card.style.transform = `rotateX(${-(y - r.height / 2) / 18}deg) rotateY(${(x - r.width / 2) / 18}deg)`;
  });
  card.addEventListener("mouseleave", () => {
    card.style.transform = "rotateX(0) rotateY(0)";
  });
});
