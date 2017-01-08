#! /usr/bin/env python

from bs4 import BeautifulSoup
import requests
import os
from tqdm import tqdm

url = "https://www.raspberrypi.org/magpi-issues/"

html = requests.get(url)

soup = BeautifulSoup(html.text,"html.parser")

links = tqdm(soup.find_all('a'))


for link in links:
    pdf_name = link['href']
    if pdf_name.endswith('.pdf'):
		downloaded = open('Downloaded.txt', 'r').read()
		if pdf_name not in downloaded:
			with open(pdf_name,'wb') as f:
				r = requests.get(url+pdf_name,stream=True)
				for chunk in tqdm(r.iter_content(1024),desc="Downloading " + pdf_name):
					f.write(chunk)
				tqdm.write("Downloaded " + pdf_name)
				downloaded = open("Downloaded.txt", "a")
				downloaded.write(pdf_name + '\n')
		
		
else:
	print "All files have been downloaded"

