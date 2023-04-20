
// Load navbar_no_login from external file
fetch('navbar_no_login.html')
.then(response => response.text())
.then(data => {
  document.querySelector('#navbar_no_login-placeholder').innerHTML = data;
})
.catch(error => console.error(error));

// Function to make Back to top button appear
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("back-to-top").style.display = "block";
  } else {
    document.getElementById("back-to-top").style.display = "none";
  }
}

// function to move page back to top
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}