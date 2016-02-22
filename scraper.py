import scraperwiki
import lxml.html
from BeautifulSoup import BeautifulSoup
import urllib2


# TAG = "/wiki/Wikipedia:Wikipedia_Signpost/2016"
# URL0 = "https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/Archives/2016"
# html = scraperwiki.scrape(URL0)
# root = lxml.html.fromstring(html)
# vs_raw = [(x.text, x.get('href')) for x in root.cssselect("a")]
# vs = [v for v in vs_raw if v[0] and v[1].count(TAG) > 0]

BASEURL = "https://en.wikipedia.org"
URL = "https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost"
html = urllib2.urlopen(URL).read()
obj = BeautifulSoup(html)
base = obj.findAll('div', id='mw-content-text')[0]
vs = [{'name': x.span.text, 'url': BASEURL + x['href']} for x in base.findAll('a') if x['href'].count('/wiki/Wikipedia:Wikipedia_Signpost/20') and x.span]

print 'Found {0} new items.'.format(len(vs))
#
# # Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(unique_keys=['name'], data=vs)
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
