function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    //center: {lat: -33.9, lng: 151.2}
    elementType: 'labels',
    stylers: [{visibility: 'off'}],
    center: {lat: 32.717738, lng: -117.164540}
  });


  setMarkers(map);
}

      // Data for the markers consisting of a name, a LatLng and a zIndex for the
      // order in which these markers should display on top of each other.

var shape = {
  coords: [1, 1, 1, 20, 18, 20, 18, 1],
  type: 'poly'
};

function setMarkers(map) {
  $.ajax({
    url: "https://fair-block.herokuapp.com/api/empty/"
  }).then(function(data) {
    greenflags = data;

    var greenimage = {
      //url: 'https://developers.google.com/maps/documentation/javascript/examples/full/greenimages/rgreenflagflag.png',
      url: 'https://i.imgur.com/0lPSdkl.png',
      // This marker is 20 pixels wide by 32 pixels high.
      size: new google.maps.Size(20, 32),
      // The origin for this greenimage is (0, 0).
      origin: new google.maps.Point(0, 0),
      // The anchor for this greenimage is the base of the flagpole at (0, 32).
      anchor: new google.maps.Point(0, 32)
    };

    for (var i = 0; i < greenflags.length; i++) {
      var greenflag = greenflags[i];
      var marker = new google.maps.Marker({
        position: {lat: parseFloat(greenflag.latitude), lng: parseFloat(greenflag.longitude)},
        map: map,
        icon: greenimage,
        shape: shape,
        title: greenflag.name + "\nPrice: $" + greenflag.price + "/hour\nEnforced: " + greenflag.days_enforced + " " + greenflag.start_enforcing + "-" + greenflag.stop_enforcing + "\nMax Time: " + greenflag.max_hours + " hours",
        //zIndex: greenflag[3]
      });
    }
  });

  $.ajax({
    url: "https://fair-block.herokuapp.com/api/full/"
  }).then(function(data) {
    redflags = data;

    var redimage = {
      //url: 'https://developers.google.com/maps/documentation/javascript/examples/full/redimages/redflagflag.png',
      url: 'https://i.imgur.com/4bcnFvY.png',
      // This marker is 20 pixels wide by 32 pixels high.
      size: new google.maps.Size(20, 32),
      // The origin for this redimage is (0, 0).
      origin: new google.maps.Point(0, 0),
      // The anchor for this redimage is the base of the flagpole at (0, 32).
      anchor: new google.maps.Point(0, 32)
    };
    // Shapes define the clickable region of the icon. The type defines an HTML
    // <area> element 'poly' which traces out a polygon as a series of X,Y points.
    // The final coordinate closes the poly by connecting to the first coordinate.
    var shape = {
      coords: [1, 1, 1, 20, 18, 20, 18, 1],
      type: 'poly'
    };
    for (var i = 0; i < redflags.length; i++) {
      var redflag = redflags[i];
      $.ajax({
        url: "https://fair-block.herokuapp.com/api/status/" + redflag.uuid
      }).then(function(data) {
        var state = data[0];
        var time_taken = state.time_in.split("T")[1].replace("Z", "");
        console.log(time_taken);
        var hour, minute, second = time_taken.split(":")

        var marker = new google.maps.Marker({
          position: {lat: parseFloat(redflag.latitude), lng: parseFloat(redflag.longitude)},
          map: map,
          icon: redimage,
          shape: shape,
          title: redflag.name + "\nTaken at" + state.time_in,
          //zIndex: redflag[3]
          //content: "HELLO"
        });
      });
    }
  });
}
