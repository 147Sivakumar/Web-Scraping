
import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0.0.0 Safari/537.36"
}

try:
    response = requests.get(URL, headers=headers, timeout=10)

    # Check the status before parsing the page
    if response.status_code != 200:
        print(f"Failed to fetch the page. Status: {response.status_code}")
    else:
        soup = BeautifulSoup(response.text, "html.parser")

        # Select headline elements from the page
        items = soup.select("h2")

        headlines = []
        seen = set()

        for item in items:
            headline = item.get_text(" ", strip=True)

            if headline and headline not in seen:
                headlines.append(headline)
                seen.add(headline)

            if len(headlines) == 5:
                break

        if len(headlines) < 5:
            print(f"Found only {len(headlines)} unique headlines.")

        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")

except requests.RequestException as error:
    print(f"Error fetching the news page: {error}")
