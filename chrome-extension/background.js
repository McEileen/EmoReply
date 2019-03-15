document.addEventListener('DOMContentLoaded', function() {
    console.log('what is document', document);
    const button = document.getElementById('submit');
    console.log('see the button', button);
    const inputField = document.getElementById('inputField');

    button.addEventListener('click', function(event) {
        console.log('see button inside event', button)
        console.log("CLICKED THE BUTTON!")
        console.log(inputField.value);
    });
})