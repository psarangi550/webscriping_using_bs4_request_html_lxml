import requests #importing the requests module 

#here we are changing the requests headers user-agent to browser useragent to simulate the request coming from the browser instead of the python requests script 

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"
}

resp=requests.get("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",headers=headers)
#sending the get request to the server and getting the html response as return value 

#now we can fetch request header from the response object as 
print(resp.request.headers)

