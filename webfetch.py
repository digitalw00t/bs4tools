#!/usr/bin/env python3
# program: webfetch.py
# author: Draeician 2023-08-17
# Purpose: Download web pages for offline development

__VERSION__ = "v0.1.0"

from bs4 import BeautifulSoup
import requests
import argparse
from urllib.parse import urlparse

def download_page(url, file_path, debug=False):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
        if debug:
            print(f"Downloaded {url} to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
        title = soup.find('title').text
        print(f"Title of the page: {title}")

def main():
    parser = argparse.ArgumentParser(description="Download web pages for offline development.")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("urls", nargs="*", help="URLs to download")
    args = parser.parse_args()

    for url in args.urls:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.replace('.', '_')
        path = parsed_url.path.replace('/', '_').strip('_')
        file_path = f"{domain}_{path}.html" if path else f"{domain}.html"
        download_page(url, file_path, args.debug)

    # Example: Parsing the first URL
    if args.urls:
        parse_html(file_path)

if __name__ == "__main__":
    main()

