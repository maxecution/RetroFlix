// Name check
// Get the first name input element
let firstNameInput = document.getElementById('first_name');
// Add an event listener to the first name input element for when it loses focus
firstNameInput.addEventListener('blur', () => {
  // Get the value of the input
  let firstNameValue = firstNameInput.value;

  // Check if the first name contains at least one alphabetical letter and meets the length requirements
  let charRange = /^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$/u;
  let firstNameIsValid = charRange.test(firstNameValue) && firstNameValue.length >= 3 && firstNameValue.length <= 30;

  // Add or remove the appropriate classes based on the validation result
  if (firstNameIsValid) {
    // Add the 'is-valid' class to the first name input element
    firstNameInput.classList.add('is-valid');
    // Remove the 'is-invalid' class from the first name input element
    firstNameInput.classList.remove('is-invalid');
  } else {
    // Remove the 'is-valid' class from the first name input element
    firstNameInput.classList.remove('is-valid');
    // Add the 'is-invalid' class to the first name input element
    firstNameInput.classList.add('is-invalid');
  }
});

// Get the last name input element
let lastNameInput = document.getElementById('last_name');

// Add an event listener to the last name input element for when it loses focus
lastNameInput.addEventListener('blur', () => {
  // Get the value of the input
  let lastNameValue = lastNameInput.value;

  // Check if the last name contains at least one alphabetical letter, is at least 3 characters long, and no more than 30 characters
  let charRange = /^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$/u;
  let lastNameIsValid = charRange.test(lastNameValue) && lastNameValue.length >= 3 && lastNameValue.length <= 30;

  // Add or remove the appropriate classes based on the validation result
  if (lastNameIsValid) {
    // Add the 'is-valid' class to the last name input element
    lastNameInput.classList.add('is-valid');
    // Remove the 'is-invalid' class from the last name input element
    lastNameInput.classList.remove('is-invalid');
  } else {
    // Remove the 'is-valid' class from the last name input element
    lastNameInput.classList.remove('is-valid');
    // Add the 'is-invalid' class to the last name input element
    lastNameInput.classList.add('is-invalid');
  }
});


// Date of birth check
// Get the date of birth input element
let dobInput = document.getElementById('dob');
// Add an event listener to the date of birth input element for when it loses focus
dobInput.addEventListener('blur', () => {
  // Get the value of the input
  let dobValue = dobInput.value;

  // Check if the user is at least 18 years old and the date is not in the future
  let eighteenYearsAgo = new Date();
  eighteenYearsAgo.setFullYear(eighteenYearsAgo.getFullYear() - 18);
  let selectedDate = new Date(dobValue);

  let errorMessage = '';
  let dobIsValid = true;
  let dobInvalid = document.getElementById('dob-invalid');
  
  if (selectedDate > new Date()) {
    errorMessage = 'Please enter a date in the past.';
    dobIsValid = false;
  } else if (selectedDate > eighteenYearsAgo) {
    errorMessage = 'You must be at least 18 years old to register.';
    dobIsValid = false;
  }

  // Add or remove the appropriate classes and error message based on the validation result
  if (dobIsValid) {
    // Add the 'is-valid' class to the date of birth input element
    dobInput.classList.add('is-valid');
    // Remove the 'is-invalid' class from the date of birth input element
    dobInput.classList.remove('is-invalid');
    // Remove the error message
    dobInput.setCustomValidity('');
  } else {
    // Remove the 'is-valid' class from the date of birth input element
    dobInput.classList.remove('is-valid');
    // Add the 'is-invalid' class to the date of birth input element
    dobInput.classList.add('is-invalid');
    // Set the error message
    dobInvalid.innerHTML=errorMessage;
  }

  // Check if the user has entered a date
  if (dobValue === "") {
    // Set an error message
    let errorMessage = 'Please enter a valid date of birth.';
    // Add the 'is-invalid' class to the date of birth input element
    dobInput.classList.add('is-invalid');
    // Remove the 'is-valid' class from the date of birth input element
    dobInput.classList.remove('is-valid');
    // Set the error message
    dobInvalid.innerHTML = errorMessage;
  }
});


// Email criteria check
// Get the email input element
let emailInput = document.getElementById('email');
// Add an event listener to the email input element for when it loses focus
emailInput.addEventListener('blur', () => {
  // Get the value of the input
  let emailValue = emailInput.value;

  // Check if the email is valid
  let emailCharRange = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  let emailIsValid = emailCharRange.test(emailValue);

  // Add or remove the appropriate classes based on the validation result
  if (emailIsValid) {
    // Add the 'is-valid' class to the email input element
    emailInput.classList.add('is-valid');
    // Remove the 'is-invalid' class from the email input element
    emailInput.classList.remove('is-invalid');
  } else {
    // Remove the 'is-valid' class from the email input element
    emailInput.classList.remove('is-valid');
    // Add the 'is-invalid' class to the email input element
    emailInput.classList.add('is-invalid');
  }
});


// Password criteria check
// Get the password input element
let passwordInput = document.getElementById('password');
let passwordIsValid = false;

// Add an event listener to the password input element
passwordInput.addEventListener('blur', () => {
  // Get the value of the input
  let passwordValue = passwordInput.value;
  
  // Check if the password meets the criteria
  if (/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&*+,\-.:;=?@^_~])[a-zA-Z\d!#$%&*+,\-.:;<=>?@^_~]{8,}$/.test(passwordValue)) {
    // Add the 'is-valid' class to the password input element
    passwordInput.classList.add('is-valid');
    // Remove the 'is-invalid' class from the password input element
    passwordInput.classList.remove('is-invalid');
    passwordIsValid = true;
  } else {
    // Remove the 'is-valid' class from the password input element
    passwordInput.classList.remove('is-valid');
    // Add the 'is-invalid' class to the password input element
    passwordInput.classList.add('is-invalid');
    passwordIsValid = false;
  }
});

// Password match check
// Get the password input elements
let passwordCheckInput = document.getElementById('password_check');
let passwordCheckIsValid = false;

// Add an event listener to the password check input element
passwordCheckInput.addEventListener('blur', () => {
  // Get the value of the password and password check inputs
  let passwordValue = passwordInput.value;
  let passwordCheckValue = passwordCheckInput.value;

  // Check if the passwords match
  if (passwordValue === passwordCheckValue) {
    // Add the 'is-valid' class to the password check input element
    passwordCheckInput.classList.add('is-valid');
    passwordCheckIsValid = true;
    // Remove the 'is-invalid' class from the password check input element
    passwordCheckInput.classList.remove('is-invalid');
  } else {
    // Remove the 'is-valid' class from the password check input element
    passwordCheckInput.classList.remove('is-valid');
    // Add the 'is-invalid' class to the password check input element
    passwordCheckInput.classList.add('is-invalid');
    passwordCheckIsValid = false;

  }
});


// Pin criteria check
// Get the pin input element
let pinInput = document.getElementById('pin');
let pinIsValid = true;

pinInput.addEventListener("input", function () {
  // Remove all non-numeric characters from the input value, i.e. only let user input numbers
  let trimmedValue = this.value.replace(/[^0-9]/gi, "");

  // Set the value of the ccNumberInput field to the formatted value
  this.value = trimmedValue;
});

pinInput.addEventListener('blur', () =>{

  if (pinInput.value == "" || pinInput.value.length < 4){
    pinInput.classList.add('is-invalid');
    pinIsValid = false;
    pinInput.classList.remove('is-valid');
  } else {
    pinInput.classList.remove('is-invalid');
    pinInput.classList.add('is-valid');
    pinIsValid = true;
  }


});

// Subs selection validation
// Get the subs-select element
let subsSelect = document.getElementById('subs-select');

// Add an event listener to the subs-select element for when it changes
subsSelect.addEventListener('input', () => {
  validateSubscription();
});

// Add an event listener to the subs-select element for when it loses focus
subsSelect.addEventListener('blur', () => {
  validateSubscription();
});

function validateSubscription() {
  // Get the selected option's value
  let selectedOption = subsSelect.value;

  // Check if the selected option is valid
  let subsIsValid = selectedOption === 'monthly' || selectedOption === 'yearly';

  // Add or remove the appropriate classes based on the validation result
  if (subsIsValid) {
    // Add the 'is-valid' class to the select element
    subsSelect.classList.add('is-valid');
    // Remove the 'is-invalid' class from the select element
    subsSelect.classList.remove('is-invalid');
  } else {
    // Remove the 'is-valid' class from the select element
    subsSelect.classList.remove('is-valid');
    // Add the 'is-invalid' class to the select element
    subsSelect.classList.add('is-invalid');
  }
}


// CC Name
// Get the first name input element
let ccNameInput = document.getElementById('cc-name');
// Add an event listener to the first name input element for when it loses focus
ccNameInput.addEventListener('blur', () => {
  // Get the value of the input
  let ccNameValue = ccNameInput.value;

  // Check if the first name contains at least one alphabetical letter and meets the length requirements
  let charRange = /^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$/u;
  let ccNameIsValid = charRange.test(ccNameValue) && ccNameValue.length >= 3 && ccNameValue.length <= 30;

  // Add or remove the appropriate classes based on the validation result
  if (ccNameIsValid) {
    // Add the 'is-valid' class to the first name input element
    ccNameInput.classList.add('is-valid');
    // Remove the 'is-invalid' class from the first name input element
    ccNameInput.classList.remove('is-invalid');
  } else {
    // Remove the 'is-valid' class from the first name input element
    ccNameInput.classList.remove('is-valid');
    // Add the 'is-invalid' class to the first name input element
    ccNameInput.classList.add('is-invalid');
  }
});


// CC Number
// Get the cc-number element
let ccNumberInput = document.getElementById("cc-number");

ccNumberInput.addEventListener("input", function () {
  // Remove all non-numeric characters from the input value, i.e. only let user input numbers
  let trimmedValue = this.value.replace(/[^0-9]/gi, "");

  // Add a space after every 4 characters
  trimmedValue = trimmedValue.replace(/(.{4})/g, "$1 ");

  // Trim the string to a maximum length of 19 characters, removing the final space
  trimmedValue = trimmedValue.substr(0, 19);

  // Set the value of the ccNumberInput field to the formatted value
  this.value = trimmedValue;
});

ccNumberInput.addEventListener("blur", function () {

  let ccNumberIsValid = this.value.length == 19

  if (ccNumberIsValid) {
    // Add the 'is-valid' class to the cc number input element
    ccNumberInput.classList.add('is-valid');
    // Remove the 'is-invalid' class from the cc number input element
    ccNumberInput.classList.remove('is-invalid');
  } else {
    // Remove the 'is-valid' class from the cc number input element
    ccNumberInput.classList.remove('is-valid');
    // Add the 'is-invalid' class to the cc number input element
    ccNumberInput.classList.add('is-invalid');
  }

});


// CC Expiry
// Get the cc-expiry element
let ccExpiryInput = document.getElementById("cc-expiry");

ccExpiryInput.addEventListener("input", function () {

  // Remove all non-numeric characters from the input value, i.e. only let user input numbers
  let trimmedValue = this.value.replace(/[^0-9]/gi, "");

  // If the length of the trimmed value is greater than 2, add a slash after the second character to format the value as MM/YY
  if (trimmedValue.length > 2) {
    const month = trimmedValue.substr(0, 2);
    const year = trimmedValue.substr(2);
    trimmedValue = `${month}/${year}`;
  }

  // Set the value of the ccExpiryInput field to the formatted value
  this.value = trimmedValue;
});

ccExpiryInput.addEventListener("blur", function () {

  let ccExpiryIsValid = this.value.length == 5

  if (ccExpiryIsValid) {
    // Add the 'is-valid' class to the cc number input element
    ccExpiryInput.classList.add('is-valid');
    // Remove the 'is-invalid' class from the cc number input element
    ccExpiryInput.classList.remove('is-invalid');
  } else {
    // Remove the 'is-valid' class from the cc number input element
    ccExpiryInput.classList.remove('is-valid');
    // Add the 'is-invalid' class to the cc number input element
    ccExpiryInput.classList.add('is-invalid');
  }

});

// CC CVV
//Get the cc-cvv element
let ccCVVInput = document.getElementById("cc-cvv")

ccCVVInput.addEventListener("input", function () {

  // Remove all non-numeric characters from the input value, i.e. only let user input numbers
  let trimmedValue = this.value.replace(/[^0-9]/gi, "");
  this.value = trimmedValue;

});

ccCVVInput.addEventListener("blur", function () {

  let ccCVVIsValid = this.value.length == 3

  if (ccCVVIsValid) {
    // Add the 'is-valid' class to the cc number input element
    ccCVVInput.classList.add('is-valid');
    // Remove the 'is-invalid' class from the cc number input element
    ccCVVInput.classList.remove('is-invalid');
  } else {
    // Remove the 'is-valid' class from the cc number input element
    ccCVVInput.classList.remove('is-valid');
    // Add the 'is-invalid' class to the cc number input element
    ccCVVInput.classList.add('is-invalid');
  }

});

// Checks before "Sign Up" can be submitted


let tcConfirmCheckbox = document.getElementById('tc-confirm')

let signUpBtn = document.getElementById('sign_up_btn');

signUpBtn.addEventListener('click', function(event) {

  // Check if all fields are valid and the checkbox is checked
  if (!(firstNameInput.classList.contains('is-valid') && lastNameInput.classList.contains('is-valid') && 
      dobInput.classList.contains('is-valid') && emailInput.classList.contains('is-valid') && 
      passwordInput.classList.contains('is-valid') && passwordCheckInput.classList.contains('is-valid') && 
      pinInput.classList.contains('is-valid') && subsSelect.classList.contains('is-valid') && ccNameInput.classList.contains('is-valid') && 
      ccNumberInput.classList.contains('is-valid') && ccExpiryInput.classList.contains('is-valid') && tcConfirmCheckbox.checked)) {
    //Show error messages for invalid fields
    event.preventDefault(); // Prevent form submission
    alert('Please fill in all details correctly.');
  }
});
