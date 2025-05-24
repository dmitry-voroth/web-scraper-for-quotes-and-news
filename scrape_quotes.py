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

def parse_quote(quote: BeautifulSoup) -> Tuple[str, str, str, str]:
    """
    Parse a single quote to extract text, author, tags, and author bio link.
    
    Args:
        quote: BeautifulSoup object representing a quote.
        
    Returns:
        Tuple containing (text, author, tags, author_bio_link).
    """
    text_element = quote.find('span', class_='text')
    text = text_element.text.strip('“”') if text_element else "N/A"
    
    author_element = quote.find('small', class_='author')
    author = author_element.text if author_element else "N/A"
    
    tag_elements = quote.find_all('a', class_='tag')
    tags = ', '.join(tag_element.text for tag_element in tag_elements) or "N/A"
    
    bio_link_element = quote.find('a', href=True, string=lambda s: 'about' in s.lower() if s else False)
    bio_link = bio_link_element['href'] if bio_link_element else "N/A"
    
    return text, author, tags, bio_link

def scrape_quotes(url: str, output_file: Path, max_quotes: int = 10) -> List[str]:
    """
    Scrape quotes from the given URL and return formatted quote strings.
    
    Args:
        url: The URL of the quotes website.
        output_file: Path object for the output file.
        max_quotes: Maximum number of quotes to scrape (default: 10).
        
    Returns:
        List of formatted quote strings.
    """
    soup = fetch_page(url)
    quotes = soup.find_all('div', class_='quote')[:max_quotes]
    
    formatted_quotes = []
    for i, quote in enumerate(quotes, 1):
        text, author, tags, bio_link = parse_quote(quote)
        formatted_string = f"{i}. Quote: {text} — Author: {author} — Tags: {tags} — Bio Link: {bio_link}"
        formatted_quotes.append(formatted_string)
        print(formatted_string)
    
    return formatted_quotes

def write_to_file(formatted_quotes: List[str], output_file: Path) -> None:
    """
    Write formatted quotes to the specified file.
    
    Args:
        formatted_quotes: List of formatted quote strings.
        output_file: Path object for the output file.
    """
    with output_file.open('w', encoding='utf-8') as f:
        f.write('\n'.join(formatted_quotes) + '\n')

def main():
    """Main function to execute the quote scraping process."""
    url = 'https://quotes.toscrape.com/'
    output_file = Path('quotes.txt')
    
    try:
        formatted_quotes = scrape_quotes(url, output_file)
        write_to_file(formatted_quotes, output_file)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()