from lxml import etree #importing the etree module from lxml
tree = etree.parse("/mnt/c/Users/611903295/Downloads/web_scripting_using_bs4_request_html/python_request_lxml_splash/webpage.html")
#fetching the element tree object from the parse() of the etree module
li_elements = tree.xpath("//ul/li")
#fetching all the list elements by using the xpath function
# for li in li_elements:
#     a_element=li.find("a")
#     if a_element is None:
#         print(f"{li.text.strip()}")
#     else:
#         print(f"{li.text.strip()} {a_element.text.strip()}")

#alternate approach
for li in li_elements:
    text="".join(li.xpath(".//text()"))
    print(text)