import requests
from bs4 import BeautifulSoup
from typing import List, Tuple
from pathlib import Path

def fetch_page(url: str, headers: dict = None) -> BeautifulSoup:
    """
    Fetch the webpage and return a BeautifulSoup object.
    
    Args:
        url: The URL of the webpage to fetch.
        headers: Optional headers for the HTTP request.
        
    Returns:
        BeautifulSoup object for parsing the page.
        
    Raises:
        requests.RequestException: If the request fails.
    """
    if headers is None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/129.0.0.0 Safari/537.36"
        }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for bad status codes
    return BeautifulSoup(response.text, 'html.parser')

def parse_news_item(news_item: BeautifulSoup) -> Tuple[str, str, str]:
    """
    Parse a single news item to extract title, link, and score.
    
    Args:
        news_item: BeautifulSoup object representing a news item.
        
    Returns:
        Tuple containing (title, link, score).
    """
    link_element = news_item.find('span', class_='titleline').find('a')
    title = link_element.text.strip() if link_element else "N/A"
    link = link_element['href'] if link_element else "N/A"
    
    rating_tr = news_item.find_next('tr')
    score_element = rating_tr.find('span', class_='score') if rating_tr else None
    score = score_element.text.split()[0] if score_element and score_element.text else "0"
    
    return title, link, score

def scrape_news(url: str, output_file: Path, max_items: int = 10) -> List[str]:
    """
    Scrape news from the given URL and return formatted news items.
    
    Args:
        url: The URL of the news website.
        output_file: Path object for the output file.
        max_items: Maximum number of news items to scrape (default: 10).
        
    Returns:
        List of formatted news strings.
    """
    soup = fetch_page(url)
    news_items = soup.find_all('tr', class_='athing')[:max_items]
    
    formatted_news = []
    for i, news_item in enumerate(news_items, 1):
        title, link, score = parse_news_item(news_item)
        formatted_string = f"{i}. {title} — {link} — points: {score}"
        formatted_news.append(formatted_string)
        print(formatted_string)
    
    return formatted_news

def write_to_file(formatted_news: List[str], output_file: Path) -> None:
    """
    Write formatted news items to the specified file.
    
    Args:
        formatted_news: List of formatted news strings.
        output_file: Path object for the output file.
    """
    with output_file.open('w', encoding='utf-8') as f:
        f.write('\n'.join(formatted_news) + '\n')

def main():
    """Main function to execute the news scraping process."""
    url = 'https://news.ycombinator.com/'
    output_file = Path('news_with_scores.txt')
    
    try:
        formatted_news = scrape_news(url, output_file)
        write_to_file(formatted_news, output_file)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()