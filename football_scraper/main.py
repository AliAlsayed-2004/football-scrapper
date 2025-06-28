# main.py

from scrapers import worldfootball, besoccer
from utils import display, io

def main():
    print("🌐 Select source:")
    print("1. worldfootball.net")
    print("2. besoccer.com")
    source_choice = input("➤ Source (1 or 2): ").strip()

    date = input("📅 Enter a date (YYYY-MM-DD): ").strip()

    if source_choice == "1":
        matches = worldfootball.get_matches_by_date(date)
    elif source_choice == "2":
        matches = besoccer.get_matches_by_date(date)
    else:
        print("❌ Invalid source choice.")
        return

    if not matches:
        print("❌ No matches found for this date.")
        return

    print(f"\n📊 Total matches found: {len(matches)}\n")
    display.print_matches(matches)

    print("\n💾 How would you like to save the results?")
    print("1. CSV")
    print("2. Excel")
    print("3. Do not save")

    choice = input("➤ Your choice: ").strip()

    filename_base = f"football_scraper/data/matches_{date}_{matches[0]['source'].split('.')[0]}"
    if choice == "1":
        io.save_to_csv(matches, f"{filename_base}.csv")
    elif choice == "2":
        io.save_to_excel(matches, f"{filename_base}.xlsx")
    else:
        print("✅ Results displayed without saving.")

if __name__ == "__main__":
    main()
