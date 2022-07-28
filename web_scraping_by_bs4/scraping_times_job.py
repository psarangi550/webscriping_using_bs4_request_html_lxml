from bs4 import BeautifulSoup
import requests
import json

url="https://www.timesjobs.com/candidate/job-search.html"

data={
    "searchType":"personalizedSearch",
    "from":"submit",
    "txtKeywords":"python",
    "txtLocation":"Bengaluru",
    }

html_text=requests.get(url,params=data).text

soup=BeautifulSoup(html_text,"lxml")

print(type(soup))

ul_info=soup.find("ul",class_="new-joblist")

jobs=ul_info.find_all("li",class_="clearfix job-bx wht-shd-bx")

output=[]
for job in jobs:
    company_name=job.find("h3",class_="joblist-comp-name").text.replace(" ","").replace("\n","").replace("\r","")
    experience=job.find("ul",class_="top-jd-dtl clearfix").li.text.replace("card_travel","")
    link_to_apply=job.find("header",class_="clearfix").h2.a["href"]
    published_date=job.find("span",class_="sim-posted").span.text
    if "few" not in published_date:
        output.append({
            "company_name":company_name,
            "experience":experience,
            "published_date":published_date,
            "link_to_apply":link_to_apply
            })

with open("output.json","w") as f:
    json.dump(output,f,indent=4,sort_keys=True)
