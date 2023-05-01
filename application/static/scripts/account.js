function handleEditClick(event) {
    const field = event.target.dataset.field;
    const value = document.querySelector(`#${field}`).textContent;
    const input = prompt(`Enter a new value for ${field}:`, value);
    if (input !== null) {
       fetch(`/edit-${field}/${user_id}/`, {
          method: 'POST',
          headers: {
             'Content-Type': 'application/json',
             'X-CSRFToken': getCookie('csrftoken'),
          },
          body: JSON.stringify({ value: input }),
       })
       .then(response => response.json())
       .then(data => {
          if (data.success) {
             document.querySelector(`#${field}`).textContent = input;
          } else {
             alert('Failed to update field.');
          }
       })
       .catch(error => console.error(error));
    }
 }

 const editButtons = document.querySelectorAll('.edit-button');
editButtons.forEach(button => {
   button.addEventListener('click', handleEditClick);
});