const serverAddress = "https://localhost:8080"

document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('submit');
    const inputField = document.getElementById('inputField');

    button.addEventListener('click', function(event) {
        var parameters = {
            'input': inputField.value
        }
        $.ajax({
            type: 'POST',
            url: serverAddress + '/emoReplies',
            data: parameters,
            success: function(d) {
                document.getElementById('outputField').innerText = 'hardcoded emoreply'
                console.log(d);
            },
            error: function() {
                console.log("error");
            }
        });
    });
})