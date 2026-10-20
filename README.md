# 📰 Top 5 News Headlines

## 📌 About
A simple Python web scraping project that fetches a news website and prints the top 5 headlines using `Requests` and `BeautifulSoup`.

## 🛠️ Tools Used
- Python
- Requests
- BeautifulSoup

## ✨ Features
- Fetches news content using HTTP requests.
- Checks the response status before parsing.
- Extracts 5 unique, non-empty headlines.
- Removes extra whitespace and skips duplicates.
- Handles cases where fewer than 5 headlines are found.

## 📂 Project Structure
```text
headlines/
├── headlines.py
├── README.md
├── .gitignore
├── .gitattributes
├── important-link.txt
├── Screenshot 2026-10-16 204428.png
└── headlines.py - headlines - Visual Studio Code 2026-10-16 20-45-11.mp4
```

## ⚙️ Installation

**1. Create and navigate to the project folder**
```bash
mkdir headlines
cd headlines
```

**2. Create a virtual environment**
```bash
python -m venv venv
```

**3. Activate the environment**

Windows PowerShell:
```powershell
venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
source venv/bin/activate
```

**4. Install dependencies**
```bash
pip install requests beautifulsoup4
```

## ▶️ How to Run
Run the Python script from your terminal:

```bash
python headlines.py
```

## 📰 Sample Output

1. India’s ‘cockroach’ party founder Abhijeet Dipke detained ahead of protest
2. Zelensky says Ukraine has right to defend itself after Trump calls latest strikes a ‘disgrace’
3. Pope pictured for first time since surgery and cancer diagnosis
4. ‘Onion cartel’ in Philippines fined $28m for price shock
5. Bystander ‘heroically intervened’ after three children and teacher killed in US school shooting

## 🎯 Learning Outcomes
- Learned the basics of web scraping using Python.
- Practiced sending HTTP requests and checking response status codes.
- Used BeautifulSoup to parse HTML and extract headlines.
- Practiced cleaning text and removing duplicate entries.
- Learned to handle missing or insufficient results.

## 📤 Submission
- `headlines.py` source code uploaded to GitHub.
- Screenshot of the terminal output.
- Screen recording of the script running.
- GitHub repository link shared with the community.

---

**Assignment:** Print the Top 5 Headlines from a News Site

**Learn. Build. Operate.** 🚀
