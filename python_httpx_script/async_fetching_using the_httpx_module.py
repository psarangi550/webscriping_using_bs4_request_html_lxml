import httpx #importing the httpx module
import asyncio #importing the asyncio module
import time

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
}



async def func():
    jokes=[]
    async with httpx.AsyncClient(headers=headers) as client:
        for i in range(10):
            task=asyncio.ensure_future(get_data(client,"https://api.chucknorris.io/jokes/random"))
            resp=await task
            jokes.append(resp)
    return jokes


async def get_data(client,url):
        resp=client.get(url)
        x=await resp
        return x.json()["value"]

if __name__ =="__main__":
    t1=time.perf_counter()
    output=asyncio.run(func())
    print(output)
    t2=time.perf_counter()
    print(f"total_time={t2-t1}")
    



