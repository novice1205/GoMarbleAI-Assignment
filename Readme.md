# GoMarble AI Engineer Assignment

## Overview

This project implements an API to scrape reviews from product pages dynamically using browser automation and LLMs.

### Features
- Dynamic CSS selector identification using OpenAI.
- Browser automation with Playwright.
- Pagination handling for comprehensive data extraction.

### Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd GoMarble-AI-Assignment
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key in `.env`:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

### Usage

- **Endpoint:** `/api/reviews?page={url}`
- **Method:** `GET`
- **Response Example:**

```json
{
  "reviews_count": 100,
  "reviews": [
    {
      "title": "Great Product",
      "body": "I loved it!",
      "rating": 5,
      "reviewer": "Parth"
    }
  ]
}
```