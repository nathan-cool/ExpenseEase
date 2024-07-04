document.addEventListener('DOMContentLoaded', function () {
    const navLinks = document.querySelectorAll('.nav-link');
    const currentPath = window.location.pathname;

    navLinks.forEach((link) => {

        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }

        link.addEventListener('click', function (e) {
            // Remove active class from all links
            navLinks.forEach((item) => item.classList.remove('active'));

            // Add active class to the clicked link
            this.classList.add('active');
        });
    });
});