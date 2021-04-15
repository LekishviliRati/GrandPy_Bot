$(document).ready(function() {
	$('form').on('submit', function(event) {
        event.preventDefault();
//        console.log("OK")
        let str = document.getElementById("nameInput").value;
//        console.log(str);
        const response = document.getElementById("client-chat");
        response.innerHTML = str;
	});
});