import openai
import os

def identify_css_selectors(html_content):
    """Use OpenAI GPT to identify CSS selectors for reviews."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    prompt = (
        f"Given the following HTML content, identify CSS selectors for reviews."
        f"HTML: {html_content[:1000]}"
    )

    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=200
    )

    # Example response: {"container": ".review", "title": ".title", "body": ".body", "rating": ".rating", "reviewer": ".author"}
    return eval(response.choices[0].text.strip())