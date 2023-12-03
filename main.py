import httpx
from selectolax.parser import HTMLParser

url = "https://deadfrontier2.fandom.com/wiki/Unique_Pistol"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}


response = httpx.get(
    url,
    headers=headers,
)

# response.text is the HTMl
html = HTMLParser(response.text)

rows = html.css("table.customtable tbody tr")

pistol_names = []

for row in rows:
    # Extract pistol name if available
    pistol_name_element = row.css("th span b")
    pistol_name = pistol_name_element[0].text() if pistol_name_element else "N/A"

    if pistol_name != "N/A":
        pistol_names.append(pistol_name)

print(pistol_names)
