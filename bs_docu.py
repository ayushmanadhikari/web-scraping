import requests
from bs4 import BeautifulSoup

#tags
soup = BeautifulSoup('<p class="boldest">Extremely bold</p>', 'html.parser')
tag = soup.p
tag['new_attr'] = 'new attr'
print(tag.attrs)

#multi-valued attribute.. class
soup1 = BeautifulSoup('<p class="body strikeout" id="ayusman">something</p>', 'html.parser')
tag1 = soup1.p
print(tag1.attrs)

tag1 = soup1.p
print(tag1['class'])

#navigable string... contents between start and end tag
soup2 = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag2 = soup2.b
print(tag2.string)  #prints tag content
print(tag2['class'])    #prints value of tag dictionary/object with key class
tag2.string.replace_with('replaced string')
print(tag2.string)


#beautifulsoup object represents the parsed document as a whole. you can treat it like tag object for most parts
doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")

doc.find(text="INSERT FOOTER HERE").replace_with(footer)
print(doc)
