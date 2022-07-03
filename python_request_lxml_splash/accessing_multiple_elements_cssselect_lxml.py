from lxml import etree #importing the etree module from lxml
tree = etree.parse("/mnt/c/Users/611903295/Downloads/web_scripting_using_bs4_request_html/python_request_lxml_splash/webpage.html")
#fetching the element tree object from the parse() of the etree module
html_ele_tree=tree.getroot()
li_elements=html_ele_tree.cssselect("li")
#fetching all the li elements
for li in li_elements:
    a_elemement=li.cssselect("a")
    if len(a_elemement)!=0:
        print(f"{li.text.strip()}{a_elemement[0].text.strip()}")
    else:
        print(f"{li.text.strip()}")
    
