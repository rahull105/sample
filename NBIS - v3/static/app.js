function updateRadius(value) {
  document.getElementById("radiusValue").innerText =
    value / 1000 + " km";

  const params = new URLSearchParams(window.location.search);
  params.set("radius", value);
  window.location.search = params.toString();
}

function filterCards() {
  const search = document.getElementById("searchInput").value.toLowerCase();
  const category = document.getElementById("categoryFilter").value;

  document.querySelectorAll(".card").forEach(card => {
    const name = card.dataset.name;
    const cat = card.dataset.category;

    card.style.display =
      name.includes(search) &&
      (category === "all" || cat === category)
        ? "block"
        : "none";
  });
}

function sortCards() {
  const option = document.getElementById("sortOption").value;
  const container = document.getElementById("cardsContainer");
  const cards = Array.from(container.children);

  cards.sort((a, b) => {
    if (option === "distance") {
      return a.dataset.distance - b.dataset.distance;
    }
    return a.dataset.name.localeCompare(b.dataset.name);
  });

  cards.forEach(c => container.appendChild(c));
}
