function acceptCookies() {
    // Set cookie to indicate that cookies have been accepted
    document.cookie = "cookies_accepted=true; expires=Thu, 01 Jan 2099 00:00:00 UTC; path=/;";
    
    // Hide the cookie consent banner
    document.getElementById("cookie-banner").style.display = "none";
}

// Check if cookies have been accepted, if not, show the banner
if (document.cookie.indexOf("cookies_accepted=true") === -1) {
    document.getElementById("cookie-banner").style.display = "block";

}