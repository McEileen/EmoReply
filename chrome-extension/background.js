document.addEventListener('DOMContentLoaded', function() {
    console.log('what is document', document);
    var button = document.getElementById('submit');
    
    button.addEventListener('click', function(event) {
        console.log("CLICKED THE BUTTON!")
    });
})