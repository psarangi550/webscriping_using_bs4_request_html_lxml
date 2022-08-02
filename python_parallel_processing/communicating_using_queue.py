from multiprocessing import Queue
from multiprocessing import Process

queue=Queue()

def insert_val_list(list1):
    for num in list1:
        queue.put(num*num)

def print_list(list1):
    for num in list1:
        if not queue.empty():
            print(queue.get())


list1=[1,2,3,4,5,6,7,8,9]

ps1=Process(target=insert_val_list,args=(list1,))
ps2=Process(target=print_list,args=(list1,))

ps1.start()
ps2.start()

ps1.join()
ps2.join()
