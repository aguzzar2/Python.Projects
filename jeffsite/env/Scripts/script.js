document.addEventListener("DOMContentLoaded", function () {
    // ...

    // Get all buttons with the class "table-button"
    const tableButtons = document.querySelectorAll(".table-button");

    // Add a click event listener to each table button
    tableButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            // Get the value from the button's data attribute
            const selectedTable = button.getAttribute("data-table");

            // Get the stored selected database value
            selectedDb = document.getElementById("selectedDb").value;

            fetch('http://localhost:5000/table?requestDb=' + selectedDb + '&requestTable=' + selectedTable)
                .then((response) => {
                    // Handle the response from the server as needed
                })
                .catch((error) => {
                    // Handle errors
                });
        });
    });
});
