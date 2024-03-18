const users_name = document.getElementById('users_name');
const email = document.getElementById('email');
const users_password = document.getElementById('password');
const feedback = document.getElementsByClassName('invalid-feedback');
const showPassword = document.getElementsByClassName('showPasswordToggle')[0];


showPassword.addEventListener('click', (e) => {
 

  if (showPassword.textContent === 'SHOW') {
    showPassword.textContent = 'HIDE';

    password.setAttribute('type', 'text');
  }
  else {
    showPassword.textContent = 'SHOW';
    password.setAttribute('type', 'password');
  }
});


users_name.addEventListener('keyup', (e) => {
  const users_nameValue = e.target.value;

  if (users_nameValue.length > 0) {
    fetch('/authentication/validate-name', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ users_name: users_nameValue }),
    }
    )
      .then((res) => res.json())
      .then((data) => {
        console.log('Success:', data);
        if (data.users_name_valid) {
          users_name.classList.add('is-valid');
          users_name.classList.remove('is-invalid');
          feedback[0].style.display = 'none';
        } else {
          users_name.classList.remove('is-valid');
          users_name.classList.add('is-invalid');
          feedback[0].style.display = 'block';
          feedback[0].innerHTML = `<p>${data.users_name_error}</p>`;
        }
      }).catch((error) => {
        console.error('Error:', error);
      });
  }
});



email.addEventListener('keyup', (e) => {
  const users_emailValue = e.target.value;

  if (users_emailValue.length > 0) {
    fetch('/authentication/validate-email', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email: users_emailValue }),
    }
    )
      .then((res) => res.json())
      .then((data) => {
        console.log('Success:', data);
        if (data.email_valid) {
          console.log('Success:', data);
          email.classList.add('is-valid');
          email.classList.remove('is-invalid');
          feedback[1].style.display = 'none';
        } else {
          email.classList.remove('is-valid');
          email.classList.add('is-invalid');
          feedback[1].style.display = 'block';
          feedback[1].innerHTML = `<p>${data.email_error}</p>`;
        }
      }).catch((error) => {
        console.error('Error:', error);
      });
  }
});

users_password.addEventListener('keyup', (e) => {
  const users_passwordValue = e.target.value;

  if (users_passwordValue.length > 0) {
    fetch('/authentication/validate-password', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ password: users_passwordValue }),
    }
    )
      .then((res) => res.json())
      .then((data) => {
        console.log('Success:', data);
        if (data.password_valid) {
          console.log('Success:', data);
          users_password.classList.add('is-valid');
          users_password.classList.remove('is-invalid');
       
          feedback[2].style.display = 'none';
       
        } else {
          users_password.classList.remove('is-valid');
          users_password.classList.add('is-invalid');
          feedback[2].style.display = 'block';
          feedback[2].innerHTML = `<p>${data.password_error}</p>`;
        }
      }).catch((error) => {
        console.error('Error:', error);
      });
  }
});