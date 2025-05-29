import React from 'react';

function CommentSection() {
  return (
    <div className="comment-section">
      <h3>Comments</h3>
      <textarea placeholder="Add a comment..."></textarea>
      <button>Post Comment</button>
    </div>
  );
}

export default CommentSection;