const users_name = document.getElementById('users_name');
const feedback = document.getElementsByClassName('invalid-feedback');

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
