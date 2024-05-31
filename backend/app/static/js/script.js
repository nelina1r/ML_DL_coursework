document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('queryForm');
    const loadingIndicator = document.getElementById('loading');
    const responseContainer = document.getElementById('response');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        loadingIndicator.style.display = 'inline-block';
        responseContainer.style.display = 'none';

        const theme = document.getElementById('theme').value;

        fetch('/query/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                theme: theme
            })
        })
        .then(response => response.json())
        .then(data => {
            loadingIndicator.style.display = 'none';

            responseContainer.style.display = 'block';
            responseContainer.innerText = data.response;
        })
        .catch(error => {
            console.error('Error:', error);
            loadingIndicator.style.display = 'none';
            responseContainer.style.display = 'block';
            responseContainer.innerText = 'An error occurred. Please try again.';
        });
    });
});
