# -*- coding: utf-8 -*-

__author__ = 'Sagacity'

import urllib2
import xml.dom.minidom

theQuery = u"{query}"
theQuery = theQuery.strip()
response = urllib2.urlopen('http://steamcn.com/forum.php?mod=guide&view=newthread&rss=1')
response = unicode(response.read(),'gbk').encode('utf-8')
response = response.replace('gbk', 'utf-8')
urldoc = xml.dom.minidom.parseString( response )

print "<?xml version=\"1.0\"?>\n<items>"
for item in urldoc.getElementsByTagName('item'):
    title = item.getElementsByTagName('title')[0].firstChild.data.replace( "&", "#" )
    link = item.getElementsByTagName('link')[0].firstChild.data.replace( "&", "&amp;" )
    author = item.getElementsByTagName('author')[0].firstChild.data.replace( "&", "#" )
    pubDate = item.getElementsByTagName('pubDate')[0].firstChild.data

    if theQuery == "new" or theQuery == "n":
        print "<item uid=\"SteamCN\" arg=\""+ link +"\">"
        print "<title>" + title.encode('utf-8') + "</title>"
        print "<subtitle>" + author.encode('utf-8')+ pubDate.encode('utf-8') + "</subtitle>"
        print '''</item>'''
print "</items>\n"