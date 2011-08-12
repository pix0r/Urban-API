#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import urllib
import json
import sys
import filecache

config = {
		"search_base": "http://www.urbandictionary.com/define.php?term="
		}

@filecache.filecache(48 * 60 * 60)
def get_definitions(phrase):
	url = config["search_base"] + urllib.quote(phrase)
	response = fetch_page(url)
	soup = BeautifulSoup(response)
	print soup.prettify()
	return parse_definitions(soup)

def clean_string(text):
	import re
	if not text: return ""
	print "text:", text
	print "type:", type(text)
	replace = [
			("&quot;", '"'),
			("&gt;", ">"),
			("&lt;", "<")
			]
	for k, v in replace: text.replace(k, v)
	text = re.sub("<br\s*\/?>", " ", text)
	text = re.sub("\s+", " ", text)
	return text

def parse_definitions(soup):
	items = []

	def_divs = soup.findAll("div", {"class": "definition"})
	for def_div in def_divs:
		item = {}

		# Definition
		item["definition"] = clean_string(def_div.string)

		# Example(s)
		ex_div = def_div.nextSibling
		if ex_div and ex_div.get("class") == "example":
			item["example"] = " ".join([str(x) for x in ex_div.contents])
			item["example"] = clean_string(item["example"])

		items.append(item)
	
	return items

def fetch_page(url):
	print "fetch_page(%s)" % url
	response = urllib.urlopen(url)
	data = response.read()
	return data

if __name__ == "__main__":
	if len(sys.argv) >= 2:
		phrase = sys.argv[1]
	else:
		phrase = "poop"

	print "Looking up", phrase
	result = get_definitions(phrase)
	print result

