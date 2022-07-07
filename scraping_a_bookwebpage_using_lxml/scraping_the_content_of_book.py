import requests #import requests module 

#fetching the http response from the server once we made a get request to the url  
resp=requests.get(url="http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")

#fetching the text respoponse by using the text property of the response
print(resp.text)

#fetching the content of the response which will be in byte format
# print(resp.content)

