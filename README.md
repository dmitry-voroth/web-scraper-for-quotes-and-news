Web Scraper for Quotes and News
This repository contains two Python scripts for web scraping: scrape_quotes.py and scrape_news.py. These scripts are designed to extract data from quotes.toscrape.com (quotes, authors, tags, and author bio links) and news.ycombinator.com (news titles, links, and scores), respectively. The scripts are modular, robust, and optimized for readability and maintainability.
Features

scrape_quotes.py:

Scrapes up to 10 quotes from quotes.toscrape.com.
Extracts quote text, author, tags, and author bio link.
Writes results to quotes.txt in a formatted manner.
Handles errors gracefully (e.g., network issues, missing elements).
Includes a User-Agent header to avoid server blocking.
Configurable URL, output file, and number of quotes.


scrape_news.py:

Scrapes up to 10 news items from news.ycombinator.com.
Extracts news title, link, and score.
Writes results to news_with_scores.txt in a formatted manner.
Robust error handling for HTTP errors and missing data.
Uses a User-Agent header for reliable requests.
Configurable URL, output file, and number of news items.


Common Features:

Modular design with separate functions for fetching, parsing, and writing data.
Type hints and docstrings for better code documentation.
Efficient file handling with single write operations.
Cross-platform file handling using pathlib.
Easy to extend for additional features or websites.



Installation

Clone the Repository:
git clone https://github.com/dmitry-voroth/web-scraper-for-quotes-and-news.git
cd web-scraper-for-quotes-and-news


Install Dependencies:Ensure you have Python 3.8+ installed. Install the required libraries using pip:
pip install requests beautifulsoup4


Verify Setup:Ensure the scripts (scrape_quotes.py and scrape_news.py) are in the project directory.


Usage
Running scrape_quotes.py
This script scrapes quotes from quotes.toscrape.com and saves them to quotes.txt.
python scrape_quotes.py

Output:

Console output: Displays each quote in the format: 1. Quote: {text} — Author: {author} — Tags: {tags} — Bio Link: {bio_link}.
File output: Saves the same formatted quotes to quotes.txt.

Running scrape_news.py
This script scrapes news from news.ycombinator.com and saves them to news_with_scores.txt.
python scrape_news.py

Output:

Console output: Displays each news item in the format: 1. {title} — {link} — points: {score}.
File output: Saves the same formatted news items to news_with_scores.txt.

Example Output
quotes.txt:
1. Quote: The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking. — Author: Albert Einstein — Tags: change, deep-thoughts, thinking, world — Bio Link: /author/Albert-Einstein
2. Quote: It is our choices, Harry, that show what we truly are, far more than our abilities. — Author: J.K. Rowling — Tags: abilities, choices — Bio Link: /author/J-K-Rowling
...

news_with_scores.txt:
1. Example News Title — https://example.com — points: 125
2. Another News Article — https://another.com — points: 89
...

Configuration
Both scripts are configurable:

URL: Change the url variable in the main function to scrape a different website (ensure the HTML structure matches).
Output File: Modify the output_file variable to save results to a different file.
Item Limit: Adjust the max_quotes or max_items parameter in the scrape_quotes or scrape_news function to scrape more or fewer items.

Error Handling

The scripts handle network errors, HTTP status errors, and missing HTML elements gracefully.
Errors are logged to the console with descriptive messages (e.g., Error: 404 Client Error: Not Found).

Extending the Scripts

Add Pagination: Modify the scrape_quotes function to follow "Next" links on quotes.toscrape.com for multiple pages.
Scrape Additional Data: Extend parse_quote to extract more details (e.g., author birth date from bio links).
Change Output Format: Modify the write_to_file function to support JSON, CSV, or other formats.
Custom Websites: Adapt the parsing logic in parse_quote or parse_news_item to scrape other websites with similar HTML structures.

Requirements

Python 3.8+
Libraries:
requests: For making HTTP requests.
beautifulsoup4: For parsing HTML content.



Notes

The scripts are designed for educational purposes and use quotes.toscrape.com, a website intended for scraping practice.
For news.ycombinator.com, be mindful of the website's terms of service and rate limits when scraping.
The User-Agent header mimics a browser to reduce the chance of being blocked, but use responsibly.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contributing
Contributions are welcome! Feel free to submit issues or pull requests for improvements, such as:

Adding support for other websites.
Enhancing error handling or output formats.
Improving performance for large-scale scraping.

Contact
For questions or suggestions, please open an issue on this repository or contact dmitryvorozthsov@gmail.com.
