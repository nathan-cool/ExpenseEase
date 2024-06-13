//DONE
// When the page finishes loading...
document.addEventListener('DOMContentLoaded', function () {
    // Get the search field element
    const searchField = document.getElementById('searchField');

    // Get the table output element
    const tableOutput = document.querySelector('.table-output');

    // Get the main table element
    const mainTable = document.querySelector('.main-table');

    // Get the table body element
    const tbody = document.querySelector('.table-body');

    // Initially hide the search result table
    tableOutput.style.display = 'none';

    // URL templates for editing and deleting expenses
    const urlTemplates = {
        editExpense: '/edit_expense/{id}',
        deleteExpense: '/delete_expense/{id}'
    };

    // Select the error display element
    const errorDisplay = document.getElementById('errorDisplay');

    // Add an event listener to the search field for keyup events
    searchField.addEventListener('keyup', (e) => {
        const searchValue = e.target.value.trim();

        if (searchValue.length > 0) {
            // Send a POST request to the server to search for expenses
            fetch('/search_expenses/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ searchText: searchValue })
            })
                .then((res) => res.json())
                .then((data) => {
                    if (data.length === 0) {
                        // If no results are found, display a message
                        tbody.innerHTML =
                            '<tr><td colspan="7">No Results</td></tr>';
                        tableOutput.style.display = 'block';
                        mainTable.style.display = 'none';
                    } else {
                        // Generate HTML for each expense and display them in the table
                        let rowsHtml = data
                            .map((item) => {
                                let truncatedDescription =
                                    item.description.length > 20
                                        ? item.description.substring(0, 20) +
                                          '...'
                                        : item.description;
                                const editUrl =
                                    urlTemplates.editExpense.replace(
                                        '{id}',
                                        item.id
                                    );
                                const deleteUrl =
                                    urlTemplates.deleteExpense.replace(
                                        '{id}',
                                        item.id
                                    );

                                return `
                            <tr>
                                <td>${truncatedDescription}</td>
                                <td>${item.amount}</td>
                                <td>${item.category}</td>
                                <td>${item.date}</td>
                                <td>${item.invoice_number}</td>
                                <td>${item.reference}</td>
                                <td>
                                    <a class="btn btn-sm btn-primary" href="${editUrl}">Edit</a>
                                    <button class="btn btn-sm btn-danger delete-btn" data-url="${deleteUrl}">Delete</button>
                                </td>
                            </tr>
                        `;
                            })
                            .join('');

                        tbody.innerHTML = rowsHtml;
                        addDeleteEventListeners();
                        tableOutput.style.display = 'block';
                        mainTable.style.display = 'none';
                    }
                    errorDisplay.style.display = 'none';
                })
                .catch((error) => {
                    // If an error occurs, display an error message
                    console.error('Error:', error);
                    errorDisplay.innerHTML =
                        'An error occurred. Please try again later.';
                    errorDisplay.style.display = 'block';
                    tableOutput.style.display = 'none';
                    mainTable.style.display = 'none';
                });
        } else {
            // If the search field is empty, display the main table
            tbody.innerHTML = '';
            tableOutput.style.display = 'none';
            mainTable.style.display = 'block';
            errorDisplay.style.display = 'none';
        }
    });

    // Function to add event listeners to delete buttons
    function addDeleteEventListeners() {
        // Add a click event listener to each delete button
        document.querySelectorAll('.delete-btn').forEach((button) => {
            button.addEventListener('click', () => {
                // Ask for confirmation before deleting an expense
                const confirmDelete = confirm(
                    'Are you sure you want to delete this expense?'
                );
                if (confirmDelete) {
                    // Redirect to the delete URL if confirmed
                    window.location.href = button.getAttribute('data-url');
                }
            });
        });
    }
});
