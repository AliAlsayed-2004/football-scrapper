# ⚽ Football Scraper

Easily fetch and save football match data from multiple sources! 🌍📅

---

## 🚀 Features
- Scrape match data by date from:
  - 🌐 [worldfootball.net](https://www.worldfootball.net)
  - 🌐 [besoccer.com](https://www.besoccer.com)
- Display results in a clean table 🗒️
- Save results as:
  - 📄 CSV
  - 📊 Excel
- Simple command-line interface 🖥️

---

## 🏁 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/football_scraper.git
   cd football_scraper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper:**
   ```bash
   python -m football_scraper.main
   ```

---

## 📝 Usage

1. **Select the data source**
   - `1` for worldfootball.net
   - `2` for besoccer.com
2. **Enter a date** in `YYYY-MM-DD` format
3. **View results** in the terminal
4. **Choose how to save**:
   - `1` for CSV
   - `2` for Excel
   - `3` to skip saving

---

## 📦 Project Structure
```
football_scraper/
├── data/                # Saved match data
├── scrapers/            # Source scrapers (worldfootball, besoccer)
├── utils/               # Display and IO utilities
├── main.py              # Main CLI entry point
├── requirements.txt     # Python dependencies
```

---

## 🛠️ Requirements
- Python 3.8+
- See `requirements.txt` for dependencies

---

## 📄 License
MIT License © 2025 Aloosh

---

## 🙌 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 💡 Example
```
🌐 Select source:
1. worldfootball.net
2. besoccer.com
➤ Source (1 or 2): 1
📅 Enter a date (YYYY-MM-DD): 2025-06-28

📊 Total matches found: 12

... [table of matches] ...

💾 How would you like to save the results?
1. CSV
2. Excel
3. Do not save
➤ Your choice: 1
```

Enjoy scraping! ⚽🎉
---

## 📬 Contact

- 👤 **Aloosh**
- 💼 [LinkedIn](www.linkedin.com/in/ali-alsayed-cse)
- 🐙 [GitHub](https://github.com/AliAlsayed-2004)
- ✉️ Email: alialasyed.business@gmail.com

