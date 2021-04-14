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
				$('#successAlert').hide();
			}
			else {
//			    const map = new Map(data.latitude, data.longitude);
			    let old_text = $('#successAlert').text() + "<br>"
			    let new_text = old_text + data.description
// new_text permet de ne pas perdre l'historique des question,
// sauf si rechargement de la page.
			    $('#successAlert').html(new_text).show();
				$('#errorAlert').hide();
			}
		});
	});
});