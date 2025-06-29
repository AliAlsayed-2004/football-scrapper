# main.py

from scrapers import worldfootball, besoccer
from utils import display, io
from utils.styles import Colors, CliStyle



cli_style = CliStyle()

def main():
    cli_style.print_logo()
    print(f"{Colors.LYEL}[+] Select source:")
    print(f"{Colors.CYA}[$] 1. worldfootball.net")
    print(f"{Colors.CYA}[$] 2. besoccer.com")
    source_choice = input(f"\n{Colors.YEL}[$] Source (1 or 2): ").strip()

    date = input(f"{Colors.YEL}[?] Enter a date (YYYY-MM-DD): ").strip()

    if source_choice == "1":
        matches = worldfootball.get_matches_by_date(date)
    elif source_choice == "2":
        matches = besoccer.get_matches_by_date(date)
    else:
        print(f"{Colors.RED}[-] Invalid source choice.")
        return

    if not matches:
        print(f"{Colors.RED}[-] No matches found for this date.")
        return

    print(f"{Colors.BLU}[*] Total matches found: {len(matches)}\n")
    display.print_matches(matches)

    print(f"\n{Colors.MAG}[*] How would you like to save the results?")
    print(f"{Colors.CYA}[$] 1. CSV")
    print(f"{Colors.CYA}[$] 2. Excel") 
    print(f"{Colors.CYA}[$] 3. Do not save")

    choice = input(f"\n{Colors.YEL}[?] Your choice: ").strip()

    filename_base = f"football_scraper/data/matches_{date}_{matches[0]['source'].split('.')[0]}"
    if choice == "1":
        io.save_to_csv(matches, f"{filename_base}.csv")
    elif choice == "2":
        io.save_to_excel(matches, f"{filename_base}.xlsx")
    else:
        print(f"{Colors.GRE}[*] Results displayed without saving.")

if __name__ == "__main__":
    main()
