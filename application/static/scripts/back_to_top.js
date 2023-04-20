/*

In each HTML page where you want to use the "back to top" button:

Add this in head/CSS section:

  <link rel="stylesheet" href="{{ url_for('static', filename='/styles/back_to_top.css') }}" >





And this before the closing </body> tag:

  <button onclick="topFunction()" id="back-to-top" title="Go to top">
      <svg xmlns="http://www.w3.org/2000/svg" width="25" height="45" fill="currentColor" class="bi bi-arrow-bar-up" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M8 10a.5.5 0 0 0 .5-.5V3.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 3.707V9.5a.5.5 0 0 0 .5.5zm-7 2.5a.5.5 0 0 1 .5-.5h13a.5.5 0 0 1 0 1h-13a.5.5 0 0 1-.5-.5z"/>
      </svg>
  </button>

  <script src="{{ url_for('static', filename='/scripts/back_to_top.js') }}"></script>

*/

// Show back to top button when use has scrolled past first section
window.addEventListener('scroll', function() {
    var backToTopButton = document.getElementById('back-to-top');
    if (window.scrollY > 500) {
        backToTopButton.style.display = 'block';
    } else {
        backToTopButton.style.display = 'none';
    }
});

// Function to move user back to top when clicking on button
document.getElementById('back-to-top').addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});