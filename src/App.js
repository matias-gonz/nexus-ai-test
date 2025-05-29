import React from 'react';
import Map from './components/Map';
import Post from './components/Post';
import CommentSection from './components/CommentSection';
import SubscriptionSection from './components/SubscriptionSection';

function App() {
  const travelLocations = [
    { id: 1, lat: 51.505, lng: -0.09, title: 'London' },
    { id: 2, lat: 40.7128, lng: -74.0060, title: 'New York' },
  ];

  const postContent = {
    title: 'My Trip to London',
    content: 'This is a sample blog post about my trip to London.',
  };

  return (
    <div className="app">
      <h1>Travel Blog</h1>
      <Map locations={travelLocations} />
      <Post post={postContent} />
      <CommentSection />
      <SubscriptionSection />
    </div>
  );
}

export default App;