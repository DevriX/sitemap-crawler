from bs4 import BeautifulSoup
import requests
import csv


url="https://name-of-the-site/location-of-sitemap.xml"

sitemaps_xml=requests.get(url)

sitemaps_xml_parsed = BeautifulSoup(sitemaps_xml.content, "lxml")

sitemaps_to_be_found=sitemaps_xml_parsed.findAll('loc')

file = open('old_sitemap.csv', 'w', newline ='')

sitemaps = [];
with file:
	header = ['links']
	writer = csv.DictWriter(file, fieldnames = header)
	writer.writeheader()
	for sitemap in sitemaps_to_be_found:
		sitemaps.append( sitemap.text )

	for link_to_sitemap in sitemaps:
		print( 'Crawling: ' + link_to_sitemap );
		links_xml=requests.get(link_to_sitemap)
		links_xml_parsed = BeautifulSoup(links_xml.content, "lxml")
		links_to_be_found=links_xml_parsed.findAll('loc')
		for link in links_to_be_found:
			writer.writerow({'links' : link.text })