import React, { useState } from "react";
import axios from "axios";
import "./index.css";

function App() {
  const [url, setUrl] = useState("");
  const [reviews, setReviews] = useState([]);
  const [error, setError] = useState("");

  const fetchReviews = async () => {
    setError("");
    try {
      const response = await axios.get(`http://127.0.0.1:8000/`);
      setReviews(response.data.reviews);
    } catch (err) {
      setError("Failed to fetch reviews. Please check the URL.");
    }
  };

  return (
    <div className="app">
      <h1>Review Extractor</h1>
      <div className="form">
        <input
          type="text"
          placeholder="Enter Product Page URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button onClick={fetchReviews}>Fetch Reviews</button>
      </div>
      {error && <p className="error">{error}</p>}
      <div className="reviews">
        {reviews.length > 0 ? (
          reviews.map((review, index) => (
            <div key={index} className="review">
              <h2>{review.title}</h2>
              <p>{review.body}</p>
              <p><strong>Rating:</strong> {review.rating}</p>
              <p><strong>Reviewer:</strong> {review.reviewer}</p>
            </div>
          ))
        ) : (
          <p>No reviews to display.</p>
        )}
      </div>
    </div>
  );
}

export default App;
