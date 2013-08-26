
from urllib import urlopen
from bs4 import BeautifulSoup
import re
 

rollingStone = urlopen('http://www.rollingstone.com/siteServices/rss/musicNewsAndFeature').read()

newsFinderTitle = re.compile('<title>(.*)</title>')
newsFinderLink = re.compile('<link rel.*href="(.*)"/>')

findNewsTitle = re.findall(newsFinderTitle,rollingStone)
findNewsLink = re.findall(newsFinderLink,rollingStone)

newsIterator =[]
newsIterator[:] = range(0,8)

soupNews = BeautifulSoup(rollingStone)
 
newsTitle = soupNews.findAll("title")
newsLink = soupNews.findAll("link")

for i in newsIterator:
	print newsTitle
	print newsLink
	print "\n"
	#print findNewsTitle[i]
	#print findNewsLink[i]
	#print "\n"

