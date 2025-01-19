# Reviews Scraper Frontend

This is the frontend application for interacting with the Reviews Scraper API. The UI allows users to input product page URLs, fetch reviews using the API, and display the reviews in a user-friendly format.


## Project Structure

```
frontend/
├── public/
│   └── index.html        # Main HTML file for the app
├── src/
│   ├── App.js            # Main app component
│   ├── index.js          # Entry point for the React app
│   └── index.css        # Styles for the application
├── package.json          # Project dependencies and scripts
└── README.md             # Documentation for the project
```

## Getting Started

### Prerequisites

Make sure you have the following installed:
- [Node.js](https://nodejs.org/) (version 16+ recommended)
- [npm](https://www.npmjs.com/) (comes with Node.js)


### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd frontend
   ```

2. Install the dependencies:
   ```bash
   npm install
   ```

### Running the Application

To start the development server, run:
```bash
npm start
```

This will start the React app, and you can access it at `http://localhost:3000` in your web browser.


### Usage

1. Enter a product page URL in the input field.
2. Click the "Fetch Reviews" button.
3. The application will call the Reviews Scraper API and display the reviews in a list format below the input field.


## Components

### 1. ReviewForm.jsx
- Handles user input for the product page URL.
- Triggers the API call when the "Fetch Reviews" button is clicked.

### 2. ReviewList.jsx
- Displays the list of reviews fetched from the API.
- Each review includes the title, body, rating, and reviewer name.


## Styling

- The application styles are written in `index.css`.
- You can customize the design by modifying this file.


## API Integration

The frontend interacts with the backend API to fetch reviews. Update the API base URL in `ReviewForm.jsx` if needed:
```javascript
const API_BASE_URL = "http://127.0.0.1:8000/api/reviews";
```

---

## Scripts

### Development
Start the development server:
```bash
npm start
```