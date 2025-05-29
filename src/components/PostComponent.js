import React from 'react';

const PostComponent = () => {
  return (
    <div style={{ margin: '20px', padding: '10px', border: '1px solid #ddd', backgroundColor: '#f9f9f9' }}>
      <h2>Sample Blog Post</h2>
      <p>
        This is a sample blog post about traveling. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      </p>

      {/* Comment Section */}
      <h3>Comments</h3>
      <div style={{ marginBottom: '10px' }}>
        <input type="text" placeholder="Add a comment" style={{ marginRight: '10px' }} />
        <button>Post</button>
      </div>

      {/* Subscription Section */}
      <h3>Subscribe</h3>
      <div style={{ marginBottom: '10px' }}>
        <input type="email" placeholder="Enter your email" style={{ marginRight: '10px' }} />
        <button>Subscribe</button>
      </div>
    </div>
  );
};

export default PostComponent;
