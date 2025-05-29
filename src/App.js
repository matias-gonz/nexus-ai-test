import React from 'react';
import MapComponent from './components/MapComponent';
import PostComponent from './components/PostComponent';

const App = () => {
  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px', backgroundColor: '#e0f2f7', color: '#0d47a1' }}>
      <h1>Travel Blog</h1>
      <MapComponent />
      <PostComponent />
    </div>
  );
};

export default App;
