// Get DOM elements
const users_name = document.getElementById('users-name'); // User name input field
const email = document.getElementById('email'); // Email input field
const users_password = document.getElementById('password'); // Password input field
const feedback = document.getElementsByClassName('invalid-feedback'); // Invalid feedback elements
const showPassword = document.getElementById('show-password-toggle'); // Show/hide password toggle button
const registerButton = document.getElementById('register'); // Register button

// Call the validation functions for each input field
validateName(users_name);
validateEmail(email);
validatePassword(users_password);

// Call other functions
showPasswordToggle();

// Event listener for show/hide password toggle
function showPasswordToggle() {
	showPassword.addEventListener('click', (e) => {
		e.preventDefault();
		showPassword.style.color = 'black';
		if (users_password.getAttribute('type') === 'password') {
			users_password.setAttribute('type', 'text'); // Show password
		} else {
			users_password.setAttribute('type', 'password'); // Hide password
		}
	});
}

// Event listener for user name input
function validateName(users_name) {
	users_name.addEventListener('keyup', (e) => {
		const users_nameValue = e.target.value;

		if (users_nameValue.length > 0) {
			fetch('/authentication/validate-name', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ users_name: users_nameValue })
			})
				.then((res) => res.json())
				.then((data) => {
					if (data.users_name_valid) {
						users_name.classList.add('is-valid');
						users_name.classList.remove('is-invalid');
						feedback[0].style.display = 'none'; // Hide invalid feedback
						registerButton.disabled = false; // Enable register button
					} else {
						users_name.classList.remove('is-valid');
						users_name.classList.add('is-invalid');
						feedback[0].style.display = 'block'; // Show invalid feedback
						feedback[0].innerHTML = `<p>${data.users_name_error}</p>`; // Display error message
						registerButton.disabled = true; // Disable register button
					}
				})
				.catch((error) => {
					console.error('Error:', error);
				});
		} else {
			users_name.classList.remove('is-valid');
			users_name.classList.remove('is-invalid');
			feedback[0].style.display = 'none'; // Hide invalid feedback
		}
	});
}

// Event listener for email input
function validateEmail(email) {
	email.addEventListener('keyup', (e) => {
		const emailValue = e.target.value;

		if (emailValue.length > 0) {
			fetch('/authentication/validate-email', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ email: emailValue })
			})
				.then((res) => res.json())
				.then((data) => {
					if (data.email_valid) {
						email.classList.add('is-valid');
						email.classList.remove('is-invalid');
						feedback[1].style.display = 'none'; // Hide invalid feedback
						registerButton.disabled = false; // Enable register button
					} else {
						email.classList.remove('is-valid');
						email.classList.add('is-invalid');
						feedback[1].style.display = 'block'; // Show invalid feedback
						feedback[1].innerHTML = `<p>${data.email_error}</p>`; // Display error message
						registerButton.disabled = true; // Disable register button
					}
				})
				.catch((error) => {
					console.error('Error:', error);
				});
		} else {
			email.classList.remove('is-valid');
			email.classList.remove('is-invalid');
			feedback[1].style.display = 'none'; // Hide invalid feedback
		}
	});
}

// Event listener for password input
function validatePassword(users_password) {
	users_password.addEventListener('keyup', (e) => {
		const users_passwordValue = e.target.value;

		if (users_passwordValue.length > 0) {
			showPassword.style.color = 'black';
			fetch('/authentication/validate-password', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ password: users_passwordValue })
			})
				.then((res) => res.json())
				.then((data) => {
					if (data.password_valid) {
						users_password.classList.add('is-valid');
						users_password.classList.remove('is-invalid');
						feedback[2].style.display = 'none'; // Hide invalid feedback
						registerButton.disabled = false; // Enable register button
					} else {
						users_password.classList.remove('is-valid');
						users_password.classList.add('is-invalid');
						feedback[2].style.display = 'block'; // Show invalid feedback
						feedback[2].innerHTML = `<p>${data.password_error}</p>`; // Display error message
						registerButton.disabled = true; // Disable register button
					}
				})
				.catch((error) => {
					console.error('Error:', error);
				});
		} else {
			users_password.classList.remove('is-valid');
			users_password.classList.remove('is-invalid');
			feedback[2].style.display = 'none'; // Hide invalid feedback
			showPassword.style.color = 'gray';
			showPassword.style.cursor = 'default';
			showPassword.disabled = true;
			users_password.setAttribute('type', 'password');
		}
	});
}