// hides sensitive data with '*'

const passwordEls = document.querySelectorAll('#password, #pin, #cards');
passwordEls.forEach(passwordEl => {
  passwordEl.innerText = '*'.repeat(8);

});

function showDeleteForm() {
  
  document.querySelector('#delete-form').style.display = 'block';
}

function confirmDelete() {
  return confirm('Are you sure you want to delete your account? Once deleted, your details will be permanently removed.');
}

// for cookie preferences
document.getElementById('sign_outButton').addEventListener('click', function() {

  // Remove the 'cookieSetPreferences' cookie
  document.cookie = 'cookieSetPreferences=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';

});






