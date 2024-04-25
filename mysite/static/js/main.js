document.addEventListener('DOMContentLoaded', () => {
  console.log('Hello from main.js');

  const expense_dsc = document.getElementById('expense_dsc');

  expense_dsc.addEventListener('click', () => {
    expense_dsc.innerHTML = 'Hello from main.js';
  });
});
