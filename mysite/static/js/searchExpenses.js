const searchField = document.getElementById('searchField');
const tableOutput = document.querySelector('.table-output');
const mainTable = document.querySelector('.main-table');
const tbody = document.querySelector('.table-body');
tableOutput.style.display = 'none';

searchField.addEventListener('keyup', (e) => {
  const searchValue = e.target.value;

    if (searchValue.length > 0) {
      console.log('searchValue', searchValue);
      tbody.innerHTML = '';
      

      fetch('/search_expenses/', {
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ searchText: searchValue }),
        method: 'POST',
      })
        .then((res) => res.json())
        .then((data) => {
          console.log('data', data);
          tableOutput.style.display = 'block';
          mainTable.style.display = 'none';

          if (data.length === 0) {
            tableOutput.innerHTML = 'No results found';
          }
          else {

            data.forEach((item) => {
              tbody.innerHTML += `
                  <tr>
                    <td>${item.description.substring(0, 20)}</td>
                    <td>${item.amount}</td>
                    <td>${item.category}</td>
                    <td>${item.date}</td>
                    <td>${item.invoice_number}</td>
                    <td>${item.reference}</td>
                  </tr>
              `;
            });
          }
        });
  };
    if (searchValue.length === 0) {
      tableOutput.style.display = 'none';
      mainTable.style.display = 'block';
    }
  });
