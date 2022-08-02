import asyncio #importing the asuyncio module
import datetime #importing the datetime module

count=1

def print_date():
    print(datetime.datetime.now())

def trampoline(name=""):
    global count
    print(count)
    count+=1
    print(name)
    print_date()
    loop.call_later(1,trampoline,name)


if __name__ == "__main__":
    loop=asyncio.get_event_loop()
    loop.call_soon(trampoline)
    loop.call_later(8,loop.stop)
    loop.run_forever()

    
