// hides sensitive data with '*'

const passwordEls = document.querySelectorAll('#password, #pin, #cards');
passwordEls.forEach(passwordEl => {
  passwordEl.innerText = '*'.repeat(8);

});

function validateDeleteForm() {
  var emailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  var passwordFormat = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&*+,\-.:;=?@^_~])[a-zA-Z\d!#$%&*+,\-.:;<=>?@^_~]{8,}$/;

  var userEmail = document.getElementById("email").value;
  var userPassword = document.getElementById("password").value;

  var confirmEmail = document.getElementById("confirm_email").value;
  var confirmPassword = document.getElementById("confirm_password").value;

  if (userEmail !== confirmEmail) {
      alert("Email not found.");
      return false;
  }

  if (!emailFormat.test(confirmEmail)) {
      alert("Your email address is not valid.");
      return false;
  }

  if (userPassword !== confirmPassword) {
      alert("Passwords not found.");
      return false;
  }

  if (!passwordFormat.test(confirmPassword)) {
      alert("Your password is not valid.");
      return false;
  }

  return true;
}


function showDeleteForm() {
  
  
  document.querySelector('#delete-form').style.display = 'block';
}

function confirmDelete() {
  return confirm('Are you sure you want to delete your account? Once deleted, your details will be permanently removed.');
}






