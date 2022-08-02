import asyncio #importing asyncio module

async def task1():
    print("send an email ....")
    asyncio.create_task(task2())
    await asyncio.sleep(2)
    print("got the reply from first email")


async def task2():
    print("send an second email ....")
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print("got the reply from second email")

async def task3():
    print("send third email ....")
    await asyncio.sleep(2)
    print("got the reply from third email")

if __name__ == "__main__":
    asyncio.run(task1())
    