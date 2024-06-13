//done
const users_name = document.getElementById('users_name');
const email = document.getElementById('email');
const users_password = document.getElementById('password');
const feedback = document.getElementsByClassName('invalid-feedback');
const showPassword = document.getElementById('showPasswordToggle');
const registerButton = document.getElementById('register');

validateName(users_name);
validateEmail(email);
validatePassword(users_password);
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
            feedback[0].style.display = 'none';
            registerButton.disabled = false;
          } else {
            users_name.classList.remove('is-valid');
            users_name.classList.add('is-invalid');
            feedback[0].style.display = 'block';
            feedback[0].innerHTML = `<p>${data.users_name_error}</p>`;
            registerButton.disabled = true;
          }
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    } else {
      users_name.classList.remove('is-valid');
      users_name.classList.remove('is-invalid');
      feedback[0].style.display = 'none';
    }
  });
}

// Event listener for email input
function validateEmail(email) {
  email.addEventListener('keyup', (e) => {
    const users_emailValue = e.target.value;
    if (users_emailValue.length > 0) {
      fetch('/authentication/validate-email', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: users_emailValue })
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.email_valid) {
            email.classList.add('is-valid');
            email.classList.remove('is-invalid');
            feedback[1].style.display = 'none';
            registerButton.disabled = false;
          } else {
            email.classList.remove('is-valid');
            email.classList.add('is-invalid');
            feedback[1].style.display = 'block';
            feedback[1].innerHTML = `<p>${data.email_error}</p>`;
            registerButton.disabled = true;
          }
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    } else {
      email.classList.remove('is-valid');
      email.classList.remove('is-invalid');
      feedback[1].style.display = 'none';
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
            feedback[2].style.display = 'none';
            registerButton.disabled = false;
          } else {
            users_password.classList.remove('is-valid');
            users_password.classList.add('is-invalid');
            feedback[2].style.display = 'block';
            feedback[2].innerHTML = `<p>${data.password_error}</p>`;
            registerButton.disabled = true;
          }
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    } else {
      users_password.classList.remove('is-valid');
      users_password.classList.remove('is-invalid');
      feedback[2].style.display = 'none';
      showPassword.style.color = 'gray';
      showPassword.style.cursor = 'default';
      showPassword.disabled = true;
      users_password.setAttribute('type', 'password');
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
						feedback[0].style.display = 'none';
						registerButton.disabled = false;
					} else {
						users_name.classList.remove('is-valid');
						users_name.classList.add('is-invalid');
						feedback[0].style.display = 'block';
						feedback[0].innerHTML = `<p>${data.users_name_error}</p>`;
						registerButton.disabled = true;
					}
				})
				.catch((error) => {
					console.error('Error:', error);
				});
		} else {
			users_name.classList.remove('is-valid');
			users_name.classList.remove('is-invalid');
			feedback[0].style.display = 'none';
		}
	});
}

// Event listener for email input
function validateEmail(email) {
	email.addEventListener('keyup', (e) => {
		const users_emailValue = e.target.value;

		if (users_emailValue.length > 0) {
			fetch('/authentication/validate-email', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ email: users_emailValue })
			})
				.then((res) => res.json())
				.then((data) => {
					if (data.email_valid) {
						email.classList.add('is-valid');
						email.classList.remove('is-invalid');
						feedback[1].style.display = 'none';
						registerButton.disabled = false;
					} else {
						email.classList.remove('is-valid');
						email.classList.add('is-invalid');
						feedback[1].style.display = 'block';
						feedback[1].innerHTML = `<p>${data.email_error}</p>`;
						registerButton.disabled = true;
					}
				})
				.catch((error) => {
					console.error('Error:', error);
				});
		} else {
			email.classList.remove('is-valid');
			email.classList.remove('is-invalid');
			feedback[1].style.display = 'none';
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
						feedback[2].style.display = 'none';
						registerButton.disabled = false;
					} else {
						users_password.classList.remove('is-valid');
						users_password.classList.add('is-invalid');
						feedback[2].style.display = 'block';
						feedback[2].innerHTML = `<p>${data.password_error}</p>`;
						registerButton.disabled = true;
					}
				})
				.catch((error) => {
					console.error('Error:', error);
				});
		} else {
			users_password.classList.remove('is-valid');
			users_password.classList.remove('is-invalid');
			feedback[2].style.display = 'none';
			showPassword.style.color = 'gray';
			showPassword.style.cursor = 'default';
			showPassword.disabled = true;
			users_password.setAttribute('type', 'password');
		}
	});
}
