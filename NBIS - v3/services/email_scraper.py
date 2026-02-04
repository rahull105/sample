import requests
import re
from bs4 import BeautifulSoup

def scrape_contact_details(url):
    if not url:
        return None, None

    try:
        r = requests.get(url, timeout=6, headers={
            "User-Agent": "Mozilla/5.0"
        })
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text(" ")

        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )

        phones = re.findall(
            r"\+?\d[\d\s\-]{8,}\d",
            text
        )

        email = emails[0] if emails else None
        phone = phones[0] if phones else None

        return email, phone

    except:
        return None, None
