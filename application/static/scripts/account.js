const passwordEls = document.querySelectorAll('#password, #pin, #cards');
passwordEls.forEach(passwordEl => {
  const passwordValue = passwordEl.innerText;
  passwordEl.innerText = '*'.repeat(8);
});
