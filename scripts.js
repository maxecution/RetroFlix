// Load navbar from external file
fetch('navbar.html')
.then(response => response.text())
.then(data => {
  document.querySelector('#navbar-placeholder').innerHTML = data;
})
.catch(error => console.error(error));

// Load footer from external file
fetch('footer.html')
.then(response => response.text())
.then(data => {
  document.querySelector('#footer-placeholder').innerHTML = data;
})
.catch(error => console.error(error));