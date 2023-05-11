// hides sensitive data with '*'

const passwordEls = document.querySelectorAll('#password, #pin, #cards');
passwordEls.forEach(passwordEl => {
  passwordEl.innerText = '*'.repeat(8);

});

function validateDeleteForm() {
  var emailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

  var userEmail = document.getElementById("confirm_email").value;
  var userPassword = document.getElementById("confirm_password").value;

  var confirmEmail = document.getElementById("email").textContent;
  var confirmHashedPassword = document.getElementById("password").textContent;

  if (userEmail !== confirmEmail) {
      alert("Emails do not match.");
      return false;
  }

  if (!emailFormat.test(userEmail)) {
      alert("Your email address is not valid.");
      return false;
  }

  // Hash the user's input password using SHA-256
  var hashedPassword = crypto.subtle.digest("SHA-256", new TextEncoder().encode(userPassword)).then(function(hash) {
      var hexHash = Array.from(new Uint8Array(hash)).map(b => b.toString(16).padStart(2, "0")).join("");
      return hexHash;
  });

  // Compare the hashed password with the stored hashed password
  hashedPassword.then(function(hash) {
      if (hash !== confirmHashedPassword) {
          alert("Passwords do not match.");
          return false;
      } else {
          return true;
      }
  }).catch(function(err) {
      console.error(err);
      return false;
  });
}

function showDeleteForm() {
  
  
  document.querySelector('#delete-form').style.display = 'block';
}

function confirmDelete() {
  return confirm('Are you sure you want to delete your account? Once deleted, your details will be permanently removed.');
}






