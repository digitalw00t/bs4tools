#!/usr/bin/env python3
# program: contentextractor.py
# author: Draeician 2023-08-17
# Purpose: Extract specific content from HTML files for exploration and analysis

__VERSION__ = "v0.1.0"

import requests
from bs4 import BeautifulSoup
import argparse
import os

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_content(soup, tag, attrs=None):
    results = []
    for item in soup.find_all(tag, attrs=attrs):
        results.append(str(item))
    return results

def search_string(soup, search_text):
    results = []
    for element in soup.find_all(True):
        if search_text in str(element):
            attrs = element.attrs if element.attrs else None
            results.append((element.name, attrs))
    return results

def interactive_mode(soup):
    print("Interactive mode: Type 'exit' to quit.")
    while True:
        query = input("> ")
        if query.lower() == "exit":
            break
        try:
            tag, attrs = query.split(", ")
            attrs = {k: v for k, v in (attr.split('=') for attr in attrs.split(' '))}
        except ValueError:
            tag, attrs = query, None

        content = extract_content(soup, tag, attrs)
        for item in content:
            print(item)

def export_content(content, file_path, format):
    if format == 'text':
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in content:
                file.write(item + '\n')
    print(f"Content exported to {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Extract specific content from HTML files.")
    parser.add_argument("--file", help="HTML file to analyze")
    parser.add_argument("--url", help="URL to analyze")
    parser.add_argument("--interactive", action="store_true", help="Enable interactive mode")
    parser.add_argument("--tag", help="HTML tag to target")
    parser.add_argument("--attrs", nargs='+', help="Attributes to filter by (key=value)")
    parser.add_argument("--preview", action="store_true", help="Preview the extracted content")
    parser.add_argument("--export", choices=['text'], help="Export format")
    parser.add_argument("--output", default="output.txt", help="Output file path")
    parser.add_argument("--search", help="Search for a specific string within the HTML content")
    args = parser.parse_args()

    if args.file:
        if not os.path.exists(args.file):
            print("File not found.")
            return
        with open(args.file, 'r', encoding='utf-8') as file:
            html_content = file.read()
    elif args.url:
        html_content = fetch_html(args.url)
    else:
        print("Either file or URL must be provided.")
        return

    soup = BeautifulSoup(html_content, 'html.parser')

    if args.interactive:
        interactive_mode(soup)
        return

    if args.search:
        found_elements = search_string(soup, args.search)
        print(f"Found the string \"{args.search}\" in the following elements:\n")
        for idx, (tag, attrs) in enumerate(found_elements, 1):
            query = f"soup.find('{tag}'"
            if attrs:
                query += ", " + ', '.join([f"{k}='{v}'" for k, v in attrs.items()])
            query += ")"
            print(f"{idx}. Tag: {tag}, Attributes: {attrs}\n   Query: {query}\n")
        return

    attrs = {k: v for k, v in (attr.split('=') for attr in args.attrs)} if args.attrs else None
    content = extract_content(soup, args.tag, attrs)

    if args.preview:
        for item in content:
            print(item)

    if args.export:
        export_content(content, args.output, args.export)

if __name__ == "__main__":
    main()

