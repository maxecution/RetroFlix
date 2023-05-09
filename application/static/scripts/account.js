const passwordEls = document.querySelectorAll('#password, #pin, #cards');
passwordEls.forEach(passwordEl => {
  passwordEl.innerText = '*'.repeat(7);

});





