from bs4 import BeautifulSoup

with open("article.html","r") as html_file:
    soup=BeautifulSoup(html_file,"lxml") 
    
print(soup)