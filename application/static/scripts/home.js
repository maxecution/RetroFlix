window.addEventListener('load', function() {
    var cookiePopup = document.getElementById('cookieAllow');
    var manageCookies = document.getElementById('manageCookies');
  
    if (!getCookie('cookieSetPreferences')) {
    cookiePopup.style.display = 'block';
    manageCookies.style.display = 'none'; // hide the manageCookies element and its child elements
  
    }
});

  document.getElementById('cookieForm_allow').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var cookiePopup = document.getElementById('cookieAllow');
    cookiePopup.style.display = 'none';
  
    document.body.style.overflow = 'auto';

  
  setCookie('cookieSetPreferences', true);

  });
  
  const manageCookiesButton = document.getElementById('manageCookiesButton');
  const manageCookies = document.getElementById('manageCookies');
  
  manageCookiesButton.addEventListener('click', function() {
    manageCookies.style.display = 'block'; 

  });
  
  document.getElementById('cookieForm_manage').addEventListener('submit', function(event) {
    event.preventDefault();
  
    var analyticsCheckbox = document.getElementById('analyticsCheckbox').checked;
    var marketingCheckbox = document.getElementById('marketingCheckbox').checked;
  
    setCookie('analytics', analyticsCheckbox);
    setCookie('marketing', marketingCheckbox);
  
    alert('Preferences saved.');

    manageCookies.style.display = 'none';

  });
  
  function setCookie(cookieName, cookieValue) {
    if (sessionStorage.getItem(cookieName) !== 'accepted') {
      var date = new Date();
      date.setTime(date.getTime() + (365 * 24 * 60 * 60 * 1000));
      var expires = "expires=" + date.toUTCString();
      document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/";
      sessionStorage.setItem(cookieName, 'accepted');
    }
  }

function getCookie(cookieName) {
  var name = cookieName + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var cookieArray = decodedCookie.split(';');
  for(var i = 0; i < cookieArray.length; i++) {
    var cookie = cookieArray[i];
    while (cookie.charAt(0) == ' ') {
      cookie = cookie.substring(1);
    }
    if (cookie.indexOf(name) == 0) {
      return cookie.substring(name.length, cookie.length);
    }
  }
  return "";
}