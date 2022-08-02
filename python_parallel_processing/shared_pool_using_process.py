import multiprocessing #importing the multiprocessing module 

def insert_data(value,list1):
    list1.append(value)
    print("new records been added .....")
    
def print_list(list1):
    for stu,mark in list1:
        print("Student is {stu} \nstudent cgpa is {mark}".format(stu=stu,mark=mark))

list1=[("abi",9),("rika",8),("gundu",8.5)]

value=("abismruta",10)

with multiprocessing.Manager() as manager:
    list1=manager.list(list1)
    value=("abismruta",10)
    ps1=multiprocessing.Process(target=insert_data,args=(value,list1))
    ps1.start()
    ps1.join()
    ps2=multiprocessing.Process(target=print_list,args=(list1,))
    ps2.start()
    ps2.join()

print(list1)