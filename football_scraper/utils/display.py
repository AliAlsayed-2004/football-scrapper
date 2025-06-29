# utils/display.py

from tabulate import tabulate
from utils.styles import Colors

def print_matches(matches):
    if not matches:
        print(f"{Colors.RED}[-] No matches to display.")
        return

    headers = [
        f"{Colors.YEL}Time{Colors.ENDC}",
        f"{Colors.YEL}Home{Colors.ENDC}",
        f"{Colors.YEL}Away{Colors.ENDC}",
        f"{Colors.YEL}Score{Colors.ENDC}",
        f"{Colors.YEL}Competition{Colors.ENDC}"
    ]
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

