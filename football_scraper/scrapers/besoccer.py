# scrapers/besoccer.py

import requests
from bs4 import BeautifulSoup
from datetime import datetime



BASE_URL = "https://www.besoccer.com/livescore/{date}"


def get_matches_by_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")
        return []

    url = BASE_URL.format(date=date_str)
    response = requests.get(url)
    if response.status_code != 200:
        print(f"❌ Failed to fetch page: {url}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    matches = []

    for panel in soup.select("div.panel"):
        comp_tag = panel.select_one(".panel-title span")
        competition = comp_tag.get_text(strip=True) if comp_tag else "Unknown Competition"

        for match in panel.select("a.match-link"):
            try:
                teams = match.select(".team-name")
                if len(teams) < 2:
                    continue

                team_home = teams[0].get_text(strip=True)
                team_away = teams[1].get_text(strip=True)

                time_tag = match.select_one(".marker")
                time = time_tag.get_text(strip=True) if time_tag else ""

                score = "-"
                if ':' not in time:
                    score = time
                    time = ""

                    
                matches.append({
                    "date": date_str,
                    "time": time,
                    "team_home": team_home,
                    "team_away": team_away,
                    "score": score,
                    "competition": competition,
                    "source": "besoccer.com"
                })
            except Exception as e:
                print(f"⚠️ Error parsing match: {e}")
                continue

    return matches
