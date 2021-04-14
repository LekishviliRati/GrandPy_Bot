//// Initialize and add the map : Une fonction rédigée en "JavaScript"
//function initMap(lat, lng) {
//    // The location of Paris
//    let position = { lat: lat, lng: lng};
//    // The map, centered at Paris
//    const map = new google.maps.Map(document.getElementById("map"), {
//      zoom: 7,
//      center: position
//    });
//    // The marker, positioned at Paris
//    const marker = new google.maps.Marker({
//      position: position,
//      map: map,
//    });
//};

$(document).ready(function() {

function initMap(lat, lng) {
    // The location of Paris
    let position = { lat: lat, lng: lng};
    // The map, centered at Paris
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 7,
      center: position
    });
    // The marker, positioned at Paris
    const marker = new google.maps.Marker({
      position: position,
      map: map,
    });
};
	$('form').on('submit', function(event) {
        event.preventDefault();
        $.ajax({
			data : {
				input : $('#nameInput').val(),
			},
			type : 'POST',
			url : 'http://127.0.0.1:5000/exemple'
		})
		.done(function(data) {
		    console.log(data)
		});
	});
});


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