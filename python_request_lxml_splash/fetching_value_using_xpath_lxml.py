from lxml import etree #importing the etree module from lxml package
tree=etree.parse("/mnt/c/Users/611903295/Downloads/web_scripting_using_bs4_request_html/python_request_lxml_splash/webscraper.html")
#fetching the element treee object using the parse() in etree module 
title_elemets=tree.xpath("//title")
#using the xpath() on the element tree object which provide list of element object 
print(title_elemets[0].text)
#fetching the text using the text property along with indexing 

#alternate approach is to use the text() inside the xpath() on the element tree
title_elemets_text=tree.xpath("//title/text()")[0]
#here fetchign the text of the tittle element using the indexing and text()
#as we know xpath of title will be //title[text()="Hello World"]
print(title_elemets_text)

#similarly fetching the <h1> tag value will be 
h1_elements=tree.xpath("//body/h1")
#fetching the list_of_elements will h1_elements
print(h1_elements[0].text)#fetching the text as 

#we can use the alternate way to fetch as below 
h1_elements_text=tree.xpath("//body/h1/text()")[0]
#fetching the element using the text() as above
print(h1_elements_text)  



