import re

def validate_url(url):
    """Validate the provided URL."""
    pattern = re.compile(
        r'^(http://www\.|https://www\.|http://|https://)?[a-z0-9]+([\-\.]?[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(/.*)?$')
    return bool(pattern.match(url))