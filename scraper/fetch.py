import requests

HEADERS = {"User-Agent": "hn-trend-tracker (student project)"}

def get_front_page_html():
    resp = requests.get("https://news.ycombinator.com/", headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.text