from bs4 import BeautifulSoup

def parse_front_page(html):
    soup = BeautifulSoup(html, "html.parser")
    stories = soup.find_all("tr", class_="athing")

    results = []
    for story in stories:
        title_tag = story.find("span", class_="titleline").a
        title = title_tag.text
        link = title_tag.get("href")
        results.append({"title": title, "link": link})

    return results

from bs4 import BeautifulSoup
import re

def parse_front_page(html):
    soup = BeautifulSoup(html, "html.parser")
    stories = soup.find_all("tr", class_="athing")

    results = []
    for story in stories:
        title_tag = story.find("span", class_="titleline").a
        title = title_tag.text
        link = title_tag.get("href")
        story_id = story.get("id")

        # points/comments live in the NEXT row, not this one
        subtext_row = story.find_next_sibling("tr")
        subtext = subtext_row.find("td", class_="subtext")

        score_tag = subtext.find("span", class_="score") if subtext else None
        points = int(re.sub(r"\D", "", score_tag.text)) if score_tag else 0

        comment_link = subtext.find_all("a")[-1] if subtext else None
        comment_text = comment_link.text if comment_link else "0"
        comments = int(re.sub(r"\D", "", comment_text)) if "comment" in comment_text else 0

        results.append({
            "story_id": story_id,
            "title": title,
            "link": link,
            "points": points,
            "comments": comments,
        })

    return results