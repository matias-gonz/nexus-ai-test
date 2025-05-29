import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

// Fix for Leaflet marker icon issue
delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

const MapComponent = () => {
  // Example travel locations
  const locations = [
    { id: 1, name: 'Paris', lat: 48.8566, lng: 2.3522 },
    { id: 2, name: 'Tokyo', lat: 35.6895, lng: 139.6917 },
    { id: 3, name: 'New York', lat: 40.7128, lng: -74.0060 },
  ];

  return (
    <MapContainer center={[40, 0]} zoom={2} style={{ height: '400px', width: '100%' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {locations.map(location => (
        <Marker key={location.id} position={[location.lat, location.lng]}>
          <Popup>
            {location.name}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

export default MapComponent;
