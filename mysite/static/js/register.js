// Done 
// Initial setup for elements and feedback messages
const users_name = document.getElementById('users_name'); // Get the input field for the user's name
const email = document.getElementById('email'); // Get the input field for the email
const users_password = document.getElementById('password'); // Get the input field for the password
const feedback = document.querySelectorAll('.invalid-feedback'); // Get all the feedback elements
const showPassword = document.getElementById('showPasswordToggle'); // Get the password visibility toggle button
const registerButton = document.getElementById('register'); // Get the register button

// Validation and Event Listener Functions
function setupEventListeners() {
  users_name.addEventListener('keyup', () => validateName()); // Listen for keyup event on the user's name input field
  email.addEventListener('keyup', () => validateEmail()); // Listen for keyup event on the email input field
  users_password.addEventListener('keyup', () => validatePassword()); // Listen for keyup event on the password input field
  showPassword.addEventListener('click', togglePasswordVisibility); // Listen for click event on the password visibility toggle button
}

function validateName() {
  const users_nameValue = users_name.value; // Get the value of the user's name input field
  const feedbackElement = feedback[0]; // Get the first feedback element

  if (users_nameValue.length > 0) {
    // If the user's name is not empty
    postData('/authentication/validate-name', {
      users_name: users_nameValue
    })
      .then((data) =>
        updateUI(
          data,
          users_name,
          feedbackElement,
          'users_name_valid',
          'users_name_error'
        )
      )
      .catch((error) => console.error('Error:', error));
  } else {
    resetValidation(users_name, feedbackElement); // Reset the validation state of the user's name input field
  }
}

function validateEmail() {
  const users_emailValue = email.value; // Get the value of the email input field
  const feedbackElement = feedback[1]; // Get the second feedback element

  if (users_emailValue.length > 0) {
    // If the email is not empty
    postData('/authentication/validate-email', { email: users_emailValue })
      .then((data) =>
        updateUI(
          data,
          email,
          feedbackElement,
          'email_valid',
          'email_error'
        )
      )
      .catch((error) => console.error('Error:', error));
  } else {
    resetValidation(email, feedbackElement); // Reset the validation state of the email input field
  }
}

function validatePassword() {
  const users_passwordValue = users_password.value; // Get the value of the password input field
  const feedbackElement = feedback[2]; // Get the third feedback element

  updatePasswordToggle(users_passwordValue); // Update the visibility toggle button based on the password value

  if (users_passwordValue.length > 0) {
    // If the password is not empty
    postData('/authentication/validate-password', {
      password: users_passwordValue
    })
      .then((data) =>
        updateUI(
          data,
          users_password,
          feedbackElement,
          'password_valid',
          'password_error'
        )
      )
      .catch((error) => console.error('Error:', error));
  } else {
    resetValidation(users_password, feedbackElement); // Reset the validation state of the password input field
  }
}

function togglePasswordVisibility(e) {
  e.preventDefault(); // Prevent the default behavior of the click event
  if (users_password.getAttribute('type') === 'password') {
    // If the password is currently hidden
    users_password.setAttribute('type', 'text'); // Show the password
  } else {
    users_password.setAttribute('type', 'password'); // Hide the password
  }
}

function updatePasswordToggle(value) {
  showPassword.style.color = value ? 'black' : 'gray'; // Set the color of the visibility toggle button based on the password value
  showPassword.style.cursor = value ? 'pointer' : 'default'; // Set the cursor style of the visibility toggle button based on the password value
  showPassword.disabled = !value; // Disable the visibility toggle button if the password value is empty
}

function postData(url, data) {
  return fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  }).then((res) => res.json());
}

function updateUI(data, element, feedbackElement, validKey, errorKey) {
  if (data[validKey]) {
    // If the data indicates that the input is valid
    element.classList.add('is-valid'); // Add the 'is-valid' class to the input field
    element.classList.remove('is-invalid'); // Remove the 'is-invalid' class from the input field
    feedbackElement.style.display = 'none'; // Hide the feedback message
    registerButton.disabled = false; // Enable the register button
  } else {
    element.classList.remove('is-valid'); // Remove the 'is-valid' class from the input field
    element.classList.add('is-invalid'); // Add the 'is-invalid' class to the input field
    feedbackElement.style.display = 'block'; // Show the feedback message
    feedbackElement.innerHTML = `<p>${data[errorKey]}</p>`; // Set the feedback message text
  }
}

function resetValidation(element, feedbackElement) {
  element.classList.remove('is-valid'); // Remove the 'is-valid' class from the input field
  element.classList.remove('is-invalid'); // Remove the 'is-invalid' class from the input field
  feedbackElement.style.display = 'none'; // Hide the feedback message
}

document.addEventListener('DOMContentLoaded', () => {
  setupEventListeners(); // Set up event listeners when the DOM is loaded
});
