import os
import requests
from bs4 import BeautifulSoup

def fetch_web_page(target_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(target_url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as error:
        print(f"Error fetching the URL: {error}")
        return None

def parse_headlines(html_content):
    if not html_content:
        return []
    
    soup = BeautifulSoup(html_content, "html.parser")
    headlines_list = []
    
    for item in soup.find_all("span", class_="titleline"):
        text = item.get_text(strip=True)
        if text:
            headlines_list.append(text)
            
    return headlines_list

def save_headlines_to_file(headlines):
    if not headlines:
        print("No headlines found to save.")
        return
        
    filename = "scraped_headlines.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("--- Algohub Internship Week 5: Scraped Headlines ---\n\n")
        for index, headline in enumerate(headlines, start=1):
            file.write(f"{index}. {headline}\n")
            
    print(f"Successfully saved {len(headlines)} headlines to {filename}")

def main():
    target_url = "https://news.ycombinator.com/"
    print(f"Starting web scraping for: {target_url}")
    
    html_data = fetch_web_page(target_url)
    extracted_headlines = parse_headlines(html_data)
    
    for i, h in enumerate(extracted_headlines[:10], 1):
        print(f"{i}. {h}")
        
    save_headlines_to_file(extracted_headlines)

if __name__ == "__main__":
    main()