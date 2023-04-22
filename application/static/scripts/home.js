window.addEventListener('load', function() {
    var cookiePopup = document.getElementById('cookieAllow');
    var manageCookies = document.getElementById('manageCookies');

    cookiePopup.style.display = 'block';
    manageCookies.style.display = 'block';
  });
  
  document.getElementById('cookieForm_allow').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var cookiePopup = document.getElementById('cookieAllow');
    cookiePopup.style.display = 'none';
  
    document.body.style.overflow = 'auto';
  });

  const manageCookiesButton = document.getElementById('manageCookiesButton');
  const manageCookies = document.getElementById('manageCookies');
  
  manageCookiesButton.addEventListener('click', function() {
    manageCookies.classList.toggle('d-none');
  });

  document.getElementById('cookieForm_manage').addEventListener('submit', function(event) {
    event.preventDefault();
  
    var analyticsCheckbox = document.getElementById('analyticsCheckbox').checked;
    var marketingCheckbox = document.getElementById('marketingCheckbox').checked;

    setCookie('analytics', analyticsCheckbox);
    setCookie('marketing', marketingCheckbox);
  
    alert('Preferences saved.');
  });



function setCookie(cookieName, cookieValue) {
    var date = new Date();
    date.setTime(date.getTime() + (365 * 24 * 60 * 60 * 1000)); // 1 year
    var expires = "expires=" + date.toUTCString();
    document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/";
}