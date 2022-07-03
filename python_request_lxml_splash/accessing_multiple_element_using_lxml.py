from lxml import etree #importing the etree module from lxml
tree=etree.parse("/mnt/c/Users/611903295/Downloads/web_scripting_using_bs4_request_html/python_request_lxml_splash/webpage.html")
#fetching the element tree object from the etree module
#fetching all the li_element objects from the body of the html
li_elements=tree.findall("body/ul/li")
#iterating through all the li elements
# for li in li_elements:
#     print(li.text)
#the above code will not fetch the <a> tag content which is insude the <li> tag
#for that we need to use the find() on the element object
for li in li_elements:
    a_element_obj=li.find('a')
    if a_element_obj is not None:
        print(f"{li.text.strip()} {a_element_obj.text}")
    else:
        print(f"{li.text.strip()}")

