# utils/display.py

from tabulate import tabulate


def print_matches(matches):
    if not matches:
        print("No matches to display.")
        return

    headers = ["Time", "Home", "Away", "Score", "Competition"]
    table = [
        [
            match["time"],
            match["team_home"],
            match["team_away"],
            match["score"],
            match["competition"],
        ]
        for match in matches
    ]

    print(tabulate(table, headers=headers, tablefmt="grid"))

