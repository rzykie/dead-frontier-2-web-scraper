import httpx
from selectolax.parser import HTMLParser

url = "https://deadfrontier2.fandom.com/wiki/Skills"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}