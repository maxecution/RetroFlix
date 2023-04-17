// Get the date 18 years ago
var eighteenYearsAgo = new Date();
eighteenYearsAgo.setFullYear(eighteenYearsAgo.getFullYear() - 18);

// Add event listener to the date input field
document.getElementById("form3Example3cg").addEventListener("change", function() {
  // Get the value of the date input field
  var inputDate = new Date(this.value);
  // Compare the input date to the date 18 years ago
  if (inputDate > eighteenYearsAgo) {
    alert("You must be 18 years or older to sign up.");
    this.value = ""; // Clear the input field
  }
});
