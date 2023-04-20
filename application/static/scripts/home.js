window.addEventListener('load', function() {
    var cookiePopup = document.getElementById('cookieAllow');
    cookiePopup.style.display = 'block';
  });
  
  document.getElementById('cookieForm_allow').addEventListener('submit', function(event) {
    event.preventDefault();
  
    var allowCheckbox = document.getElementById('allowCheckbox').checked;
  
    setCookie('allow', allowCheckbox);
    
    var cookiePopup = document.getElementById('cookieAllow');
    cookiePopup.style.display = 'none';
  
    document.body.style.overflow = 'auto';
  });

  document.getElementById('cookieForm_manage').addEventListener('submit', function(event) {
    event.preventDefault();
  
    var analyticsCheckbox = document.getElementById('analyticsCheckbox').checked;
    var marketingCheckbox = document.getElementById('marketingCheckbox').checked;
  
    setCookie('analytics', analyticsCheckbox);
    setCookie('marketing', marketingCheckbox);
  
    alert('Preferences saved!');
  });

  document.getElementById('showManageCookies').addEventListener('click', function(event) {
    event.preventDefault();
  
    var manageCookies = document.getElementById('manageCookies');
    manageCookies.style.display = 'block';
  
    this.style.display = 'none';
  });

function setCookie(cookieName, cookieValue) {
    var date = new Date();
    date.setTime(date.getTime() + (365 * 24 * 60 * 60 * 1000)); // 1 year
    var expires = "expires=" + date.toUTCString();
    document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/";
}