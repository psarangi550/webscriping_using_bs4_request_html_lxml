from unittest.mock import patch
from lxml import html #importing the html module from lxml package
import requests #importing the requests package 
import re #importing the regular expression module 
from typing import List
import json
import csv
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"
}
resp=requests.get("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",headers=headers)

#fetching the Element object by using the fromstring() from the html module of the lxml package
tree=html.fromstring(html=resp.text)

#printing the element tree object 
# print(tree)

# #from the element object we can get the title of the html as
# title_text=tree.xpath("//title/text()")[0]
# print(title_text.strip())


# #fetching the book name using the xpath as 
# book_name=tree.xpath("//div[contains(@class,'product_main')]/h1/text()")[0]
# print(book_name.strip())

# #fetching the price of the book by using the  xpath as 
# book_price=tree.xpath("//div[contains(@class,'product_main')]/p[1]/text()")[0]
# print(book_price.strip())

# #fetching the book stock using the xpath as below 
# book_stock=tree.xpath("//div[contains(@class,'product_main')]/p[2]/text()")[1]
# print(book_stock.strip())

# #fetching the product description using the xpath as below 
# book_desc=tree.xpath("//div[@id='product_description']/following::p/text()")[0]
# print(book_desc.strip())

#always have to remember that xpath will provide list of element object in return value 

#alternate approach 
product_main=tree.xpath("//div[contains(@class,'product_main')]")[0]
book_name=product_main.xpath(".//h1/text()")[0].strip()
book_price=product_main.xpath(".//p[1]/text()")[0].strip()
book_stock=product_main.xpath(".//p[2]/text()")[1].strip()
print(book_stock)
#1st approach:-
################################
# match_stock=re.search("[0-9]{2}",book_stock)
# stock=match_stock.group()
#alertnate approach:-
#########################
# match_stock=re.compile("[0-9]{2}")
# iter_stock=re.finditer(match_stock,book_stock)
# fetch_stock=None
# for stock in iter_stock:
#     fetch_stock=stock.group()
#another_alternate_approach
################################
# match_stock=re.compile("[0-9]{2}") #this will return an pattern object 
# #on this pattern object we can apply all the method 
# iter_stock=match_stock.finditer(book_stock)
# fetch_stock=None
# for stock in iter_stock:
#     fetch_stock=stock.group()
###another alternate #################################
# pattern=re.compile(r"\d+")
# fetch_stock=pattern.findall(book_stock)[0]
#implmenting_without regex
################################
def get_integer(data:str):
    result = ""
    for value in data:
        if value=="2":
            result=result+value
    return result

#alternate approach
################################################################

def get_digit(data:str):
    result = ""
    for value in data:
        try:
            int_value = int(value)
        except ValueError:
            continue
        else:
            result = result+str(int_value)
    return result

#alternate approach
################################################################
def get_easy_digit(data:str)->str:
    result=""
    for value in data:
        if value.isdigit():
            result+=str(value)
    return result

# print(get_easy_digit(book_stock))
# print(get_digit(book_stock))

####better usage by using the filter() as below######

# def get_simple_digit(data:str):
#     if data.isdigit():
#         return True
#     else:
#         return False

# fetch_stock="".join(list(filter(get_simple_digit,book_stock)))

#best use cases ######
###here we are using the lambda anonymous function instead general method usecases
fetch_stock="".join(list(filter(lambda x:x.isdigit(),book_stock)))

# fetch_stock=get_easy_digit(book_stock)
book_desc=tree.xpath("//div[@id='product_description']/following::p/text()")[0].strip()

#representing all by a dict as 
book_info={
    "name":book_name,
    "price":book_price,
    # "stock":stock,
    "stock":fetch_stock,
    "description":book_desc,
}

# print(book_info)

#writing data to the json file
with open("book.json","w") as book_json:
    json.dump(book_info, book_json,indent=2,sort_keys=False)

#writing the data into the csv file as 

with open("book.csv", 'w') as csv_file:
    headers=["name","price","stock","description"]
    csv_writer=csv.DictWriter(csv_file,fieldnames=headers,delimiter=",")
    csv_writer.writeheader()
    csv_writer.writerow(book_info)
