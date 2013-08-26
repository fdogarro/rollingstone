
from urllib import urlopen
from bs4 import BeautifulSoup
import re
 

website = urlopen('http://www.rollingstone.com/siteServices/rss/musicNewsAndFeature').read()

newsFinderTitle = re.compile('')
newsFinderLink = re.compile('<link rel.*href="(.*)">')
newFinderContent = re.compile()

findNewsTitle = re.findall(newsFinderTitle,website)
findNewsLink = re.findall(newsFinderLink,website)

newsIterator =[]
newsIterator[:] = range(0,8)

soupNews = BeautifulSoup(website)
 
newsTitle = soupNews.findAll("title")
newsLink = soupNews.findAll("link")

for i in newsIterator:
	print newsTitle
	print newsLink
	print "\n"
	#print findNewsTitle[i]
	#print findNewsLink[i]
	#print "\n"

