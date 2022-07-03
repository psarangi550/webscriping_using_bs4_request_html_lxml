from lxml import etree #importing the etree module from lxml
tree = etree.parse("/mnt/c/Users/611903295/Downloads/web_scripting_using_bs4_request_html/python_request_lxml_splash/webscraper.html")
#fetching the element tree object using the etree module parse()
html_tree = tree.getroot()
print(html_tree)
#converting the element tree to html element object on which the cssselect can work
#the cssselect() can only work on element object but not on the element treee object 
#hence we can convert the element tree object into element object using the getroot() method
title_elemets=html_tree.cssselect("title")[0]
#fetching the list of elements object in the list
print(title_elemets.text)
#fetching the title out of the first one 

#similarly we can fetch the paragraph we can use as 
p_elemets=html_tree.cssselect("h1")[0]
#fetching the list of elements object in the list format
print(p_elemets.text)
#fetch the text for the same as 