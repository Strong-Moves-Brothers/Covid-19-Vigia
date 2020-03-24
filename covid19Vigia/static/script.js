// function spanBlock(){
//     document.querySelector(".main-Div").innerHTML = "Sou GAY";
// }

// Latitude e longitude

// var x = document.getElementById("geoloc");

// function getLocation(){
//     if (navigator.geolocation){
//     navigator.geolocation.getCurrentPosition(showPosition);
//     } else {
//     x.innerHTML = "Geolocation is not supported by this browser.";
//     }
// }

// function showPosition(position) {
//     x.innerHTML = "Latitude: " + position.coords.latitude + "Longitude: " + position.coords.longitude;
// }


// // Error Treatment 
// function showError(error) {
//     switch(error.code) {
//       case error.PERMISSION_DENIED:
//         x.innerHTML = "User denied the request for Geolocation."
//         break;
//       case error.POSITION_UNAVAILABLE:
//         x.innerHTML = "Location information is unavailable."
//         break;
//       case error.TIMEOUT:
//         x.innerHTML = "The request to get user location timed out."
//         break;
//       case error.UNKNOWN_ERROR:
//         x.innerHTML = "An unknown error occurred."
//         break;
//     }
//   }
// // Show position on map
// function showPosition(position) {
//     var latlon = position.coords.latitude + "," + position.coords.longitude;

//     var img_url = "https://maps.googleapis.com/maps/api/staticmap?center="+latlon+"&zoom=14&size=400x300&sensor=false&key=YOUR_KEY";

//     document.getElementsByClassName("main-Div").innerHTML = "<img src='"+img_url+"'>";

//     open(img_url.toString,'_blank')
// }
