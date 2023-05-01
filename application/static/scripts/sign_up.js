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
const dobInput = document.getElementById('dob');
// Add an event listener to the date of birth input element for when it loses focus
dobInput.addEventListener('blur', () => {
  // Get the value of the input
  const dobValue = dobInput.value;

  // Check if the user is at least 18 years old and the date is not in the future
  const eighteenYearsAgo = new Date();
  eighteenYearsAgo.setFullYear(eighteenYearsAgo.getFullYear() - 18);
  const selectedDate = new Date(dobValue);

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
const passwordInput = document.getElementById('password');

// Add an event listener to the password input element
passwordInput.addEventListener('blur', () => {
  // Get the value of the input
  const passwordValue = passwordInput.value;

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
const passwordCheckInput = document.getElementById('password_check');

// Add an event listener to the password check input element
passwordCheckInput.addEventListener('blur', () => {
  // Get the value of the password and password check inputs
  const passwordValue = passwordInput.value;
  const passwordCheckValue = passwordCheckInput.value;

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
const pinInput = document.getElementById('pin');

// Add an event listener to the pin input element
pinInput.addEventListener('input', () => {
  // Get the value of the input
  const pinValue = pinInput.value;
  
  // Check if the value is anything but 4 numeric characters
  if (pinValue.length > 0 && (!/^\d*$/.test(pinValue) || pinValue.length > 4)) {
    // Add the 'is-invalid' class to the pin input element
    pinInput.classList.add('is-invalid');
  } else {
    // Remove the 'is-invalid' class from the pin input element
    pinInput.classList.remove('is-invalid');
  }
});