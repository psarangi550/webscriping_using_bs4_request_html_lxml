from lxml import etree #importing the etree module from lxml module
tree=etree.parse("/mnt/c/Users/611903295/Downloads/web_scripting_using_bs4_request_html/python_request_lxml_splash/webscraper.html")
#fetching the Element Tree object from the etree module from lxml package
h1_element=tree.find("body/h1")
#fetching the Element object from the Element Tree object 
print(h1_element.text)#accessing the text property
