function searchData() {
    const query = document.getElementById("search-box").value;

    // Fetch data from Flask API
    $.get(`/search?query=${query}`, function(data) {
        // Clear existing table rows
        const tbody = document.querySelector('#results-table tbody');
        tbody.innerHTML = '';

        // Populate table with new data
        data.forEach(row => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${row.id}</td>
                <td>${row.name}</td>
                <td>${row.description}</td>
            `;
            tbody.appendChild(tr);
        });
    });
}

// Initial load of data (optional)
$(document).ready(() => {
    searchData();
});