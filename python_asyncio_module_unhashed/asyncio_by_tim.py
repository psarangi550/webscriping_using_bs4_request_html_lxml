import asyncio #importing the asyncio module 

async def get_data():
    print("Fetching the data.....") 
    await asyncio.sleep(2)
    print("data been fetched ....")
    return {"data":100}

async def main():
    x=asyncio.create_task(get_data())
    await asyncio.sleep(1)
    y=await x
    print(y)

if __name__ == "__main__":
    asyncio.run(main())
