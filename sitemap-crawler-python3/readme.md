# Sitemap Crawler
This simple python script will crawl your sitemap and generate a CSV file containing all the links in the sitemap.

**It will only work with nested sitemaps!**

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

```bash
pip install beautifulsoup4
```

## Setting it up

Before running the script make sure you change the URL pointing to the sitemap

```python
url="https://name-of-the-site/location-of-sitemap.xml"
```

You can also change the location and name of the output file
```python
file = open('old_sitemap.csv', 'w', newline ='')
```

## Usage

To run the script use:
```bash
python3 crawler.py
```