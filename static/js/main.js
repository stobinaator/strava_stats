var map = L.map('map');

let vt_run_coords = {north : 43.0757, east : 25.6230};
let ka_run_coords = {north : 48.9960, east : 8.4045};
let vt_walk_coords = {north : 43.0757, east : 25.6230};
let ka_walk_coords = {north : 49.0040, east : 8.4045};


function vtRunFunction(runs){
  this.map.setView([vt_run_coords.north, vt_run_coords.east], 15);

  L.tileLayer(
      'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 18,
      }).addTo(map);

  for (let encoded of runs) {
    var coordinates = L.Polyline.fromEncoded(encoded).getLatLngs();

    L.polyline(
        coordinates,
        {
          color: 'blue',
          weight: 2,
          opacity: .7,
          lineJoin: 'round',
      }
    ).addTo(map);
  }
}


function kaRunFunction(runs){
  this.map.setView([ka_run_coords.north, ka_run_coords.east], 14);

  L.tileLayer(
      'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 18,
      }).addTo(map);


  for (let encoded of runs) {
    var coordinates = L.Polyline.fromEncoded(encoded).getLatLngs();

    L.polyline(
        coordinates,
        {
          color: 'blue',
          weight: 2,
          opacity: .7,
          lineJoin: 'round',
      }
    ).addTo(map);
  }
}


function vtWalkFunction(walks){
  this.map.setView([vt_walk_coords.north, vt_walk_coords.east], 15);

  L.tileLayer(
      'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 18,
      }).addTo(map);

  for (let encoded of walks) {
    var coordinates = L.Polyline.fromEncoded(encoded).getLatLngs();

    L.polyline(
        coordinates,
         {
        color: 'green',
        weight: 2,
        opacity: .7,
        lineJoin: 'round',
    }
    ).addTo(map);
  }
}

function kaWalkFunction(walks){
  this.map.setView([ka_walk_coords.north, ka_walk_coords.east], 14);

  L.tileLayer(
      'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 18,
      }).addTo(map);

  for (let encoded of walks) {
    var coordinates = L.Polyline.fromEncoded(encoded).getLatLngs();

    L.polyline(
        coordinates,
         {
        color: 'green',
        weight: 2,
        opacity: .7,
        lineJoin: 'round',
    }
    ).addTo(map);
  }
}