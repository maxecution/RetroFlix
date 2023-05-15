// hides sensitive data with '*'

const passwordEls = document.querySelectorAll('#password, #pin, #cards');
passwordEls.forEach(passwordEl => {
  passwordEl.innerText = '*'.repeat(8);

});

function showDeleteForm() {
  
  document.querySelector('#delete-form').style.display = 'block';
}

function confirmDelete() {
    if (confirm("Are you sure you want to delete your account?")) {
      var form = document.getElementById("delete-account-form");
      form.method = "POST";
      var methodInput = document.createElement("input");
      methodInput.setAttribute("type", "hidden");
      methodInput.setAttribute("name", "_method");
      methodInput.setAttribute("value", "DELETE");
      form.appendChild(methodInput);
      form.submit();
    }
    return false;
  }

// for cookie preferences
document.getElementById('sign_outButton').addEventListener('click', function() {

  // Remove the 'cookieSetPreferences' cookie
  document.cookie = 'cookieSetPreferences=; expires=0';

});






