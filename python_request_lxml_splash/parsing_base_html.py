from lxml import etree #importing the etree module from lxml package
tree=etree.parse("/mnt/c/Users/611903295/Downloads/web_scripting_using_bs4_request_html/python_request_lxml_splash/webscraper.html")
# print(tree)
print(etree.tostring(tree).decode('utf-8'))