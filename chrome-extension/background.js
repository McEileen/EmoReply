chrome.browserAction.onClicked.addListener(buttonClicked);

chrome.runtime.onInstalled.addListener(function() {
    var text = document.getElementById('inputField').value;
    console.log('Text', text);
    //var text = $("#myTextArea").val();
});

function buttonClicked() {
	chrome.extension.getBackgroundPage().console.log("button clicked!");
}