# AlgoHub Python Programming Internship - Week 5 Project: Web Scraping & Automation

## 📌 Project Overview
This project is developed as part of the **AlgoHub Software House Python Programming Internship Program (Week 5)**. The core objective of this week is to master **Web Scraping** and **Task Automation** by extracting data from live web pages using HTTP requests and BeautifulSoup, alongside automating routine file organization tasks using scheduled Python scripts[span_1](start_span)[span_1](end_span).

---

## 🔗 Submission & Project Links
- **GitHub Repository Link:** [https://github.com/AbdulWahabAI/AlgoHub-Python-Internship/tree/main/AlgoHub_Task5_WebScraper_Automation]
- **Live Demo Video Link:** [https://drive.google.com/file/d/1_AfFbNKnf4je_E-lOemPutN_0TKYHSPM/view?usp=drivesdk]
- **LinkedIn Post Link:** [https://www.linkedin.com/posts/abdul-wahab-1077a3291_python-webscraping-automation-ugcPost-7488515211662991362-VKcE/?utm_source=share&utm_medium=member_android&rcm=ACoAAEbGItcBzdgiKeoEnOEahLBrZMgjtIO1ItY]

---

## 🚀 Project Features
1. **Web Scraper (`scraper.py`):**
   - Securely fetches live web pages using custom HTTP headers to prevent blocking.
   - Parses HTML DOM structures efficiently using BeautifulSoup.
   - Extracts top articles/headlines and automatically writes them to an organized `.txt` output file.

2. **Task Automation (`automation.py`):**
   - Monitors a local target directory and categorizes messy files into respective folders (Documents, Images, Others) based on extensions.
   - Integrates the `schedule` library to execute background maintenance routines automatically at specified intervals.

---

## 🛠️ Models, Tools & Technology Stack
- **Programming Language:** Python 3.x[span_2](start_span)[span_2](end_span)
- **Core Libraries / Tools:**
  - `requests`: Used for sending HTTP GET requests and handling network responses[span_3](start_span)[span_3](end_span).
  - `beautifulsoup4`: Used for parsing HTML and extracting target elements via tag/class matching[span_4](start_span)[span_4](end_span).
  - `schedule`: Used for building lightweight background task schedulers[span_5](start_span)[span_5](end_span).
  - `os` & `shutil`: Built-in Python modules for directory management and file manipulation.
- **Environment & Version Control:** Git & GitHub[span_6](start_span)[span_6](end_span)

---

## ⚙️ Installation & Setup Guide

Follow these steps to run the project locally on your machine:

2. Install Dependencies
​Install all required packages listed in requirements.txt:
pip install -r requirements.txt

3. Run the Web Scraper
Execute the scraping script to fetch and save headlines:
python scraper.py

4. Run the Task Automation Scheduler
Execute the automation script to organize local folders:
python automation.py

📂 Project Structure
AlgoHub_Task5_WebScraper_Automation/
│
├── scraper.py             # Script for web data extraction & file logging
├── automation.py          # Script for scheduled directory organization
├── requirements.txt       # Project python dependencies list
└── README.md              # Project documentation and details