document.addEventListener("DOMContentLoaded", function () {
  const searchForm = document.querySelector(".df-search-form form");
  const searchInput = document.querySelector(".df-search-input input");
  const searchResults = document.createElement("div");
  searchResults.classList.add("search-results");
  document.querySelector(".df-search-form").appendChild(searchResults);

  searchForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const query = searchInput.value.toLowerCase().trim();
    searchResults.innerHTML = "";

    if (query) {
      const results = searchContent(query);
      displayResults(results);
    }
  });

  function searchContent(query) {
    const content = [
      {
        title: "Asphalt Paving",
        url: "asphalt-paving.html",
        keywords: [
          "asphalt",
          "paving",
          "installation",
          "resurfacing",
          "replacement",
          "extension",
        ],
      },
      {
        title: "Sealer",
        url: "sealer.html",
        keywords: [
          "sealcoating",
          "asphalt maintenance",
          "crack filling",
          "line striping",
        ],
      },
      {
        title: "Pavers",
        url: "Pavers.html",
        keywords: [
          "pavers installation",
          "paver maintenance",
          "retaining walls",
          "belgium blocks",
        ],
      },
      {
        title: "Concrete",
        url: "concrete.html",
        keywords: ["walkways", "sidewalks", "curbs", "aprons"],
      },
      {
        title: "Landscaping",
        url: "landscaping.html",
        keywords: [
          "sod installation",
          "top soil",
          "seed grass",
          "drainage",
          "gutters",
          "power wash",
          "hauling",
          "winter services",
        ],
      },
    ];

    return content.filter(
      (item) =>
        item.title.toLowerCase().includes(query) ||
        item.keywords.some((keyword) => keyword.toLowerCase().includes(query))
    );
  }

  function highlightKeywords(text, query) {
    const words = query.split(" ");
    let highlightedText = text;
    words.forEach((word) => {
      if (word.length > 2) {
        const regex = new RegExp(`(${word})`, "gi");
        highlightedText = highlightedText.replace(regex, "<mark>$1</mark>");
      }
    });
    return highlightedText;
  }

  function displayResults(results) {
    if (results.length > 0) {
      results.forEach((result) => {
        const resultItem = document.createElement("div");
        resultItem.classList.add("search-result-item");
        const highlightedTitle = highlightKeywords(
          result.title,
          searchInput.value
        );
        resultItem.innerHTML = `<a href="${result.url}">${highlightedTitle}</a>`;
        searchResults.appendChild(resultItem);
      });
    } else {
      searchResults.innerHTML = "<p>No results found</p>";
    }
  }

  // Close search results when clicking outside
  document.addEventListener("click", function (event) {
    if (!searchForm.contains(event.target)) {
      searchResults.innerHTML = "";
    }
  });

  // Add keyup event listener for real-time search
  searchInput.addEventListener("keyup", function () {
    const query = this.value.toLowerCase().trim();
    if (query.length >= 2) {
      const results = searchContent(query);
      displayResults(results);
    } else {
      searchResults.innerHTML = "";
    }
  });
});
