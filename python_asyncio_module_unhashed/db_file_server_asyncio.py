import asyncio #importing the asyncio module 

async def fetch_data():
    print("fetching data from the DB .....")
    await asyncio.sleep(2)
    print("data been fetched .......")
    return {"data":100}

async def print_task():
    for i in range(10,0,-1):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    #running coroutin concurrently 
    x=asyncio.create_task(fetch_data())
    y=asyncio.create_task(print_task())

    #awaiting for the responses  
    val= await x
    await y
    print(val)


print(asyncio.iscoroutine(print_task()))

if __name__ == "__main__":
    # asyncio.run(main())
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())