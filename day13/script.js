const searchBox = document.getElementById("searchBox");
const bookCards = document.querySelectorAll(".book-card");

searchBox.addEventListener("input", function () {
    const searchText = searchBox.value.toLowerCase();

    bookCards.forEach(function (card) {
        const title = card.getAttribute("data-title").toLowerCase();

        if (title.includes(searchText)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
});