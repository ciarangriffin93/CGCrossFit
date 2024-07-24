 // Center the map on Dublin, Ireland
 var map = L.map('map').setView([53.3498, -6.2603], 13);

 // Add OpenStreetMap tiles
 L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
 }).addTo(map);

 // Add a marker in Dublin
 L.marker([53.3498, -6.2603]).addTo(map)
     .bindPopup('Dublin, Ireland')
     .openPopup();