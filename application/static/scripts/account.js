const passwordEls = document.querySelectorAll('#password, #pin, #card_details');
passwordEls.forEach(passwordEl => {
  passwordEl.innerText = '*'.repeat(7);

});





