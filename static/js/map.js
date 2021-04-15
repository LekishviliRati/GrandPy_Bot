// Initialize and add the map : Une fonction rédigée en "JavaScript"
function initMap(latitude, longitude) {
    // The location of Paris
    const position = { lat: latitude, lng: longitude};
    // The map, centered at Paris
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 11,
      center: position
    });
    // The marker, positioned at Paris
    const marker = new google.maps.Marker({
      position: position,
      map: map,
    });
};

$(document).ready(function() {
	$('form').on('submit', function(event) {
        event.preventDefault();
        $.ajax({
			data : {
				input : $('#nameInput').val(),
			},
			type : 'POST',
			url : 'http://127.0.0.1:5000/bob'
		})
		.done(function(data) {
		    let latitude = parseFloat(data["latitude"])
		    let longitude = parseFloat(data["longitude"])
		    initMap(latitude, longitude)
//		    console.log(data["longitude"])
		});
	});
});



const myDiv = document.getElementById('my-div');

myDiv.innerHTML = 'Hey my name is <strong>Dom</strong>';
//export class Map {
//  constructor() {
//    this.place = {};
//    this.zoom = 7;
//  }
//
//  initMap(longitude, latitude) {
//    this.place = {
//      lat: latitude,
//      lng: longitude,
//    };
//
//    // Get a map
//    const map = new google.maps.Map(document.getElementById("map"), {
//      zoom: 7,
//      center: position
//    });
//
//    // Add marker
//    const marker = new google.maps.Marker({
//      position: position,
//      map: map,
//    });
//  }
//}

//

