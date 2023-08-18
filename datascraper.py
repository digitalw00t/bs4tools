#!/usr/bin/env python3
# program: datascraper.py
# author: Draeician 2023-08-17
# Purpose: Extract structured data from web pages

__VERSION__ = "v0.1.0"

from bs4 import BeautifulSoup
import requests
import argparse
import csv
import json

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_data(html, tag, attrs):
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    for item in soup.find_all(tag, attrs=attrs):
        row = [text.get_text().strip() for text in item.find_all(['td', 'th'])]
        data.append(row)
    return data

def export_data(data, output_format, file_path):
    if output_format == 'csv':
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    elif output_format == 'json':
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

def main():
    parser = argparse.ArgumentParser(description="Extract structured data from web pages.")
    parser.add_argument("url", help="URL to scrape")
    parser.add_argument("--tag", default="table", help="HTML tag to target")
    parser.add_argument("--attrs", nargs='+', help="Attributes to filter by (key=value)")
    parser.add_argument("--output-format", choices=['csv', 'json'], default='csv', help="Output format")
    parser.add_argument("--file", default="output.csv", help="Output file path")
    args = parser.parse_args()

    attrs = {k: v for k, v in (attr.split('=') for attr in args.attrs)} if args.attrs else None
    html = fetch_html(args.url)
    data = extract_data(html, args.tag, attrs)
    export_data(data, args.output_format, args.file)
    print(f"Data extracted and saved to {args.file}")

if __name__ == "__main__":
    main()

