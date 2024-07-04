// Get DOM elements
const userName = document.getElementById('users-name'); // User name input field
const email = document.getElementById('email'); // Email input field
const userPassword = document.getElementById('password'); // Password input field
const feedbackElements = document.getElementsByClassName('invalid-feedback'); // Invalid feedback elements
const showPasswordToggle = document.getElementById('show-password-toggle'); // Show/hide password toggle button
const registerButton = document.getElementById('register'); // Register button

// Call the validation functions for each input field
validateName(userName);
validateEmail(email);
validatePassword(userPassword);

// Call other functions
togglePasswordVisibility();

// Event listener for show/hide password toggle
function togglePasswordVisibility() {
    showPasswordToggle.addEventListener('click', (e) => {
        e.preventDefault();
        showPasswordToggle.style.color = 'black';
        if (userPassword.getAttribute('type') === 'password') {
            userPassword.setAttribute('type', 'text'); // Show password
        } else {
            userPassword.setAttribute('type', 'password'); // Hide password
        }
    });
}

// Event listener for user name input
function validateName(userName) {
    userName.addEventListener('keyup', (e) => {
        const userNameValue = e.target.value;

        if (userNameValue.length > 0) {
            fetch('/authentication/validate-name', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ users_name: userNameValue })
            })
                .then((res) => res.json())
                .then((data) => {
                    if (data.users_name_valid) {
                        userName.classList.add('is-valid');
                        userName.classList.remove('is-invalid');
                        feedbackElements[0].style.display = 'none'; // Hide invalid feedback
                        registerButton.disabled = false; // Enable register button
                    } else {
                        userName.classList.remove('is-valid');
                        userName.classList.add('is-invalid');
                        feedbackElements[0].style.display = 'block'; // Show invalid feedback
                        feedbackElements[0].innerHTML = `<p>${data.users_name_error}</p>`; // Display error message
                        registerButton.disabled = true; // Disable register button
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        } else {
            userName.classList.remove('is-valid');
            userName.classList.remove('is-invalid');
            feedbackElements[0].style.display = 'none'; // Hide invalid feedback
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
                        feedbackElements[1].style.display = 'none'; // Hide invalid feedback
                        registerButton.disabled = false; // Enable register button
                    } else {
                        email.classList.remove('is-valid');
                        email.classList.add('is-invalid');
                        feedbackElements[1].style.display = 'block'; // Show invalid feedback
                        feedbackElements[1].innerHTML = `<p>${data.email_error}</p>`; // Display error message
                        registerButton.disabled = true; // Disable register button
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        } else {
            email.classList.remove('is-valid');
            email.classList.remove('is-invalid');
            feedbackElements[1].style.display = 'none'; // Hide invalid feedback
        }
    });
}

// Event listener for password input
function validatePassword(userPassword) {
    userPassword.addEventListener('keyup', (e) => {
        const userPasswordValue = e.target.value;

        if (userPasswordValue.length > 0) {
            showPasswordToggle.style.color = 'black';
            fetch('/authentication/validate-password', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ password: userPasswordValue })
            })
                .then((res) => res.json())
                .then((data) => {
                    if (data.password_valid) {
                        userPassword.classList.add('is-valid');
                        userPassword.classList.remove('is-invalid');
                        feedbackElements[2].style.display = 'none'; // Hide invalid feedback
                        registerButton.disabled = false; // Enable register button
                    } else {
                        userPassword.classList.remove('is-valid');
                        userPassword.classList.add('is-invalid');
                        feedbackElements[2].style.display = 'block'; // Show invalid feedback
                        feedbackElements[2].innerHTML = `<p>${data.password_error}</p>`; // Display error message
                        registerButton.disabled = true; // Disable register button
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        } else {
            userPassword.classList.remove('is-valid');
            userPassword.classList.remove('is-invalid');
            feedbackElements[2].style.display = 'none'; // Hide invalid feedback
            showPasswordToggle.style.color = 'gray';
            showPasswordToggle.style.cursor = 'default';
            showPasswordToggle.disabled = true;
            userPassword.setAttribute('type', 'password');
        }
    });
}