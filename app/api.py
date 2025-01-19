from fastapi import APIRouter, HTTPException, Query
from app.scraper import scrape_reviews

router = APIRouter()

@router.get("/api/reviews")
async def get_reviews(page: str = Query(...)):
    page = page.strip()
    if not page.startswith("http"):
        raise HTTPException(status_code=400, detail="Invalid URL provided.")
    try:
        reviews_data = await scrape_reviews(page)
        return reviews_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
