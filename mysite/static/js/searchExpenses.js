const searchField = document.getElementById('searchField');
const tableOutput = document.querySelector('.table-output');
const mainTable = document.querySelector('.main-table');
const tbody = document.querySelector('.table-body');
// Initially hide the search result table
tableOutput.style.display = 'none';



searchField.addEventListener('keyup', (e) => {
    const searchValue = e.target.value.trim();  // Trim to remove any extra spaces

    if (searchValue.length > 0) { // Check if the searchValue is greater than 0
        
        fetch('/search_expenses/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ searchText: searchValue }),
        })
        .then(res => res.json())
        .then(data => {
			console.log('data', data);

	
			// Conditionally display tables based on data
			if (data.length === 0) {
				tableOutput.style.display = 'block'; // Show tableOutput to display the no results message
				mainTable.style.display = 'none'; // Hide mainTable since there are no results
                tbody.innerHTML = 'No Results' // Show no results message
            } else {
               
        tbody.innerHTML = ''; 
				let rowsHtml = data
                    .map((item) => {
                        let truncatedDescription = item.description.length > 20 ? item.description.substring(0, 20) + '...' : item.description; // Truncate the description to 20 characters
						const editUrl = urlTemplates.editExpense.replace(
							'{id}',
							item.id // Replace the {id} placeholder with the actual id
						);
						const deleteUrl = urlTemplates.deleteExpense.replace(
							'{id}', // Replace the {id} placeholder with the actual id
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
                                <a class="btn btn-sm btn-danger" href="${deleteUrl}" onclick="return confirm('Are you sure you want to delete this expense?')">Delete</a>
                            </td>
                        </tr>
                    `;
					})
                    .join('');
             
                tbody.innerHTML = rowsHtml; // Update the tbody with new rows
				tableOutput.style.display = 'block'; // Make sure to show the tableOutput with results
                mainTable.style.display = 'none'; // Hide the mainTable to only show the search results
                console.log('rowsHtml', rowsHtml);
			}
		})
        .catch(error => {
            console.error('Error:', error); // Log any errors to the console
            tableOutput.innerHTML = 'An error occurred. Please try again later.'; // Display an error message
            tableOutput.style.display = 'block'; // Show the error message
            mainTable.style.display = 'none'; // Hide the main table
        });
    } else {
        tbody.innerHTML = '';  // Clear the tbody content when there is no search input
        tableOutput.style.display = 'none';  // Hide the search results table
        mainTable.style.display = 'block';// Show the main table
      
    }
});
