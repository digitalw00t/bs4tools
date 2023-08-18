```markdown
# bs4tools

`bs4tools` is a collection of utilities designed to assist developers in working with web scraping and HTML parsing using BeautifulSoup 4 (BS4). These tools aim to provide efficient, robust, and maintainable solutions for various web scraping tasks.

## Tools Included

### 1. webfetch.py

#### Purpose

`webfetch.py` is a command-line utility for downloading web pages for offline development. It allows users to fetch HTML content from specified URLs and save them with filenames based on the domain and URL structure.

#### Features

- **Download Web Pages**: Fetch HTML content from given URLs.
- **Offline Development**: Save web pages locally for offline access.
- **Debug Mode**: Enable debug information for detailed logging.

#### Usage

##### Basic Usage

```bash
python3 webfetch.py <URL1> <URL2> ...
```

##### Enable Debug Mode

```bash
python3 webfetch.py --debug <URL1> <URL2> ...
```

##### Help Information

```bash
python3 webfetch.py --help
```

#### Requirements

- Python 3
- BeautifulSoup 4
- requests

### 2. datascraper.py

#### Purpose

`datascraper.py` is a command-line utility for extracting structured data like tables from web pages. It offers customizable targeting and multiple export options, providing flexibility in scraping various structured data.

#### Features

- **Extract Structured Data**: Target specific tags and attributes.
- **Multiple Export Options**: Supports CSV and JSON formats.
- **User-Friendly Command-Line Interface**: Customizable extraction parameters.

#### Usage

##### Basic Usage

```bash
python3 datascraper.py <URL> [--tag TAG] [--attrs ATTRS] [--output-format FORMAT] [--file FILE_PATH]
```

#### Requirements

- Python 3
- BeautifulSoup 4
- requests
- csv
- json

### 3. contentextractor.py

#### Purpose

`contentextractor.py` is a command-line utility for extracting specific content from HTML files. It enables users to explore HTML structure and identify correct tags, classes, and attributes for BeautifulSoup 4 applications.

#### Features

- **Interactive Exploration**: Query different tags, classes, and attributes to view content.
- **Batch Extraction**: Extract specific content based on user-defined parameters.
- **Preview Mode**: Preview targeted content.
- **Export Options**: Supports text format.

#### Usage

##### Interactive Mode

```bash
python3 contentextractor.py <HTML_FILE> --interactive
```

##### Batch Extraction

```bash
python3 contentextractor.py <HTML_FILE> --tag TAG [--attrs ATTRS] [--preview] [--export FORMAT]
```

#### Requirements

- Python 3
- BeautifulSoup 4

## Future Tools

1. **HTML Validator (`htmlvalidator.py`)**: Validates downloaded HTML files.
2. **Site Map Generator (`sitemapgenerator.py`)**: Creates a website's structure map.
3. **Link Checker (`linkchecker.py`)**: Validates internal and external links.
4. **Search Engine (`searchengine.py`)**: Performs keyword searches within content.
5. **Visualization Tool (`visualizationtool.py`)**: Visualizes HTML elements or extracted data.
6. **Rate Limiter (`ratelimiter.py`)**: Manages download rates.
7. **Proxy Manager (`proxymanager.py`)**: Manages proxies for anonymous scraping.
8. **User-Agent Rotator (`useragentrotator.py`)**: Rotates user-agent strings.

## Contributing

If you have ideas, suggestions, or improvements, please feel free to contribute!

## License

MIT License

## Author

Draeician, 2023

---

Designed with ❤️ for developers working with web scraping.
```
