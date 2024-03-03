document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');
  const input = document.querySelector('input[name="selection_user"]');
  const resultContainer = document.querySelector('#result-container');

  form.addEventListener('submit', function(event) {
    event.preventDefault();
    const userInput = input.value;

    fetch('/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: `selection_user=${userInput}`,
    })
    .then(response => response.text()) 
    .then(data => {
      resultContainer.innerHTML = data; 
    });
  });
});
