// Name check
// Get the first name input element
let firstNameInput = document.getElementById('first_name');
// Add an event listener to the first name input element for when it loses focus
firstNameInput.addEventListener('blur', () => {
  // Get the value of the input
  let firstNameValue = firstNameInput.value;

  // Check if the first name contains at least one alphabetical letter and meets the length requirements
  let charRange = /^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$/u;
  let isValid = charRange.test(firstNameValue) && firstNameValue.length >= 3 && firstNameValue.length <= 30;

  // Add or remove the appropriate classes based on the validation result
  if (isValid) {
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
  let isValid = charRange.test(lastNameValue) && lastNameValue.length >= 3 && lastNameValue.length <= 30;

  // Add or remove the appropriate classes based on the validation result
  if (isValid) {
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
  let isValid = true;
  let dobInvalid = document.getElementById('dob-invalid');
  
  if (selectedDate > new Date()) {
    errorMessage = 'Please enter a date in the past.';
    isValid = false;
  } else if (selectedDate > eighteenYearsAgo) {
    errorMessage = 'You must be at least 18 years old to register.';
    isValid = false;
  }

  // Add or remove the appropriate classes and error message based on the validation result
  if (isValid) {
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
  let isValid = emailCharRange.test(emailValue);

  // Add or remove the appropriate classes based on the validation result
  if (isValid) {
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
  } else {
    // Remove the 'is-valid' class from the password input element
    passwordInput.classList.remove('is-valid');
    // Add the 'is-invalid' class to the password input element
    passwordInput.classList.add('is-invalid');
  }
});

// Password match check
// Get the password input elements
let passwordCheckInput = document.getElementById('password_check');

// Add an event listener to the password check input element
passwordCheckInput.addEventListener('blur', () => {
  // Get the value of the password and password check inputs
  let passwordValue = passwordInput.value;
  let passwordCheckValue = passwordCheckInput.value;

  // Check if the passwords match
  if (passwordValue === passwordCheckValue) {
    // Add the 'is-valid' class to the password check input element
    passwordCheckInput.classList.add('is-valid');
    // Remove the 'is-invalid' class from the password check input element
    passwordCheckInput.classList.remove('is-invalid');
  } else {
    // Remove the 'is-valid' class from the password check input element
    passwordCheckInput.classList.remove('is-valid');
    // Add the 'is-invalid' class to the password check input element
    passwordCheckInput.classList.add('is-invalid');
  }
});


// Pin criteria check
// Get the pin input element
let pinInput = document.getElementById('pin');

// Add an event listener to the pin input element
pinInput.addEventListener('input', () => {
  // Get the value of the input
  let pinValue = pinInput.value;
  
  // Check if the value is anything but 4 numeric characters
  if (pinValue.length > 0 && (!/^\d*$/.test(pinValue) || pinValue.length > 4)) {
    // Add the 'is-invalid' class to the pin input element
    pinInput.classList.add('is-invalid');
  } else {
    // Remove the 'is-invalid' class from the pin input element
    pinInput.classList.remove('is-invalid');
  }
});

// Subs selection validation
// Get the subs-select element
let select = document.getElementById('subs-select');

// Add an event listener to the subs-select element for when it changes
select.addEventListener('input', () => {
  validateSubscription();
});

// Add an event listener to the subs-select element for when it loses focus
select.addEventListener('blur', () => {
  validateSubscription();
});

function validateSubscription() {
  // Get the selected option's value
  let selectedOption = select.value;

  // Check if the selected option is valid
  let isValid = selectedOption === 'monthly' || selectedOption === 'yearly';

  // Add or remove the appropriate classes based on the validation result
  if (isValid) {
    // Add the 'is-valid' class to the select element
    select.classList.add('is-valid');
    // Remove the 'is-invalid' class from the select element
    select.classList.remove('is-invalid');
  } else {
    // Remove the 'is-valid' class from the select element
    select.classList.remove('is-valid');
    // Add the 'is-invalid' class to the select element
    select.classList.add('is-invalid');
  }
}


// CC Name
// Name check
// Get the first name input element
let ccNameInput = document.getElementById('cc-name');
// Add an event listener to the first name input element for when it loses focus
ccNameInput.addEventListener('blur', () => {
  // Get the value of the input
  let ccNameValue = ccNameInput.value;

  // Check if the first name contains at least one alphabetical letter and meets the length requirements
  let charRange = /^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$/u;
  let isValid = charRange.test(ccNameValue) && ccNameValue.length >= 3 && ccNameValue.length <= 30;

  // Add or remove the appropriate classes based on the validation result
  if (isValid) {
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

  let isValid = this.value.length == 19

  if (isValid) {
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

  let isValid = this.value.length == 5

  if (isValid) {
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

  let isValid = this.value.length == 3

  if (isValid) {
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