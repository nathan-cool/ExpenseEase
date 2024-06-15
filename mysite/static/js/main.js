function updateButtonText() {
	var btn = document.querySelector('.addexpensebtn .btn');
	if (window.innerWidth <= 1068) {
		btn.textContent = 'Add';
	} else {
		btn.textContent = 'Add Expenses';
	}
}

// Run on initial load
updateButtonText();

// Run on window resize
window.addEventListener('resize', updateButtonText);
