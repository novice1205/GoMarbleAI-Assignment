from playwright.async_api import async_playwright
from app.llm_helper import identify_css_selectors

def extract_reviews(page, selectors):
    """Extract reviews dynamically based on the identified selectors."""
    reviews = []
    elements = page.query_selector_all(selectors['container'])
    for element in elements:
        reviews.append({
            "title": element.query_selector(selectors['title']).inner_text() if selectors['title'] else None,
            "body": element.query_selector(selectors['body']).inner_text() if selectors['body'] else None,
            "rating": element.query_selector(selectors['rating']).inner_text() if selectors['rating'] else None,
            "reviewer": element.query_selector(selectors['reviewer']).inner_text() if selectors['reviewer'] else None,
        })
    return reviews

async def scrape_reviews(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)

        # Extract HTML and use LLM to identify selectors
        content = await page.content()
        selectors = identify_css_selectors(content)

        # Extract reviews
        reviews = extract_reviews(page, selectors)

        await browser.close()

        return {
            "reviews_count": len(reviews),
            "reviews": reviews
        }