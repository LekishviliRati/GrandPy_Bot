$(document).ready(function() {
	$('form').on('submit', function(event) {
        event.preventDefault();
        $.ajax({
			data : {
				input : $('#nameInput').val(),
			},
			type : 'POST',
			url : 'http://127.0.0.1:5000/process'
		})
		.done(function(data) {
            console.log(data)
// Dans data on a ce que python nous retourne
// Càd : instance_wiki_description
			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#papyChat').hide();
			}
			else {
			    let old_text = $('#successAlert').text() + "<br>"
			    let new_text = old_text +
			    "Titre : " + data.title + "<br>" + "<br>" +
			    "Description: " + data.description + "<br>" + "<br>" +
			    "url: " + data.url
			    $('#successAlert').html(new_text).show();
				$('#errorAlert').hide();
			}
		});
	});
});