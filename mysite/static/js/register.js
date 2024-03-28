const users_name = document.getElementById('users_name');
const email = document.getElementById('email');
const users_password = document.getElementById('password');
const feedback = document.getElementsByClassName('invalid-feedback');
const showPassword = document.getElementsByClassName('showPasswordToggle')[0];
const registerButton = document.getElementById('register');
const googleButton = document.getElementsByClassName('g_id_signin');




// Event listener for user name input
users_name.addEventListener('keyup', (e) => {
  const users_nameValue = e.target.value;

  if (users_nameValue.length > 0) {
    fetch('/authentication/validate-name', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ users_name: users_nameValue }),
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
      }).catch((error) => {
        console.error('Error:', error);
      });
   
  }
  if (users_nameValue.length < 1) {
    users_name.classList.remove('is-valid');
    users_name.classList.remove('is-invalid');
    feedback[0].style.display = 'none';
  }
});

// Event listener for email input
email.addEventListener('keyup', (e) => {
  const users_emailValue = e.target.value;

  if (users_emailValue.length > 0) {
    fetch('/authentication/validate-email', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email: users_emailValue }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.email_valid) {
          email.classList.add('is-valid');
          email.classList.remove('is-invalid');
          registerButton.disabled = false;
          feedback[1].style.display = 'none';
          console.log("hi")
        } else {
          console.log("Hello")

          registerButton.disabled = true;
          email.classList.remove('is-valid');
          email.classList.add('is-invalid');
          feedback[1].style.display = 'block';
          feedback[1].innerHTML = `<p>${data.email_error}</p>`;
        }
      }).catch((error) => {
        console.error('Error:', error);
      });
    }
    if (users_emailValue.length < 1) {
      email.classList.remove('is-valid');
      email.classList.remove('is-invalid');
      feedback[1].style.display = 'none';
  }

});

// Event listener for password input
users_password.addEventListener('keyup', (e) => {
  
  const users_passwordValue = e.target.value;

  if (users_passwordValue.length > 0) {
    showPassword.style.color = 'black';
    fetch('/authentication/validate-password', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ password: users_passwordValue }),
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
          registerButton.disabled = true;
          feedback[2].innerHTML = `<p>${data.password_error}</p>`;
        }
      }).catch((error) => {
        console.error('Error:', error);
      });
  }
  
  if (users_passwordValue.length < 1) {
    users_password.classList.remove('is-valid');
    users_password.classList.remove('is-invalid');
    feedback[2].style.display = 'none';
    showPassword.style.color = 'gray';
    showPassword.style.cursor = 'default';
    showPassword.disabled = true;
    password.setAttribute('type', 'password');
  } else {
    // Optionally reset the color if no characters are typed
    showPassword.style.color = 'black'; // Reset to default or specify a different color
    users_password.classList.remove('is-valid');
    users_password.classList.remove('is-invalid');
    feedback[2].style.display = 'none';
    showPassword.style.cursor = 'pointer';
    showPassword.disabled = false;

  }
});


// Event listener for show/hide password toggle
showPassword.addEventListener('click', (e) => {
  e.preventDefault();
  if (password.getAttribute('type') === 'password') {
    password.setAttribute('type', 'text'); // Show password
  }
  else {
    password.setAttribute('type', 'password'); // Hide password
  }
});



// Event listener for google sign in button
googleButton.addEventListener('click', (e) => {
  e.preventDefault();

});



