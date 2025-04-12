// Auto close toggle on outside click
document.addEventListener('click', function (event) {
    const isClickInside = document.querySelector('.navbar').contains(event.target);
    const navbarCollapse = document.getElementById('myNavbar');

    if (!isClickInside && navbarCollapse.classList.contains('in')) {
      $('.navbar-toggle').click(); // triggers collapse
    }
  });