window.addEventListener('load', function() {
    var cookiePopup = document.getElementById('cookiePopup');
    cookiePopup.style.display = 'block';
});

document.getElementById('cookieForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get checkbox values
    var analyticsCheckbox = document.getElementById('analyticsCheckbox').checked;
    var personalizationCheckbox = document.getElementById('personalizationCheckbox').checked;
    var advertisingCheckbox = document.getElementById('advertisingCheckbox').checked;

    // Set cookies based on checkbox values
    setCookie('analytics', analyticsCheckbox);
    setCookie('personalization', personalizationCheckbox);
    setCookie('advertising', advertisingCheckbox);

    // Hide cookie popup
    var cookiePopup = document.getElementById('cookiePopup');
    cookiePopup.style.display = 'none';

    // Continue loading the main content of the web page
    document.body.style.overflow = 'auto';
});

function setCookie(cookieName, cookieValue) {
    var date = new Date();
    date.setTime(date.getTime() + (365 * 24 * 60 * 60 * 1000)); // 1 year
    var expires = "expires=" + date.toUTCString();
    document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/";
}