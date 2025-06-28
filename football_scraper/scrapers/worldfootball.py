# scrapers/worldfootball.py

import requests
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

BASE_URL = "https://www.worldfootball.net/matches_today/{year}/{month}/{day}/"


def get_matches_by_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        year = date_obj.strftime("%Y")
        month = date_obj.strftime("%b").lower()
        day = date_obj.strftime("%d")
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")
        return []

    url = BASE_URL.format(year=year, month=month, day=day)
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"❌ Failed to fetch page: {url}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="standard_tabelle")

    if not table:
        print(f"❌ No match data available for {date_str}.")
        return []

    matches = []
    rows = table.find_all("tr")

    for row in rows:
        comp_th = row.find("th", class_="gross")
        if comp_th:
            current_competition = comp_th.text.strip()
            continue
        cols = row.find_all("td")
        if len(cols) < 5:
            continue

        
        time = cols[0].text.strip()
        team_home = cols[1].text.strip()
        team_away = cols[3].text.strip()
        score = cols[4].text.strip()



        matches.append({
            "date": date_str,
            "time": time,
            "team_home": team_home,
            "team_away": team_away,
            "score": score,
            "competition": current_competition,
            "source": "worldfootball.net"
        })




    return matches
