from multiprocessing import Array
#importing the Array type data from multiprocessing module 
from multiprocessing import Value
#importing the Value object from multiprocessing module
import multiprocessing
#importing the multiprocessing module 
import os #importing the os module


def square_list(list1,result,sum_total):
    for i,j in enumerate(list1):
        result[i]=(j*j)
    sum_total.value=sum(result)
    print(f"result by the process-id{os.getpid()} is {list(result)}")
    print(f"sum of result  by the process-id{os.getpid()} is {sum_total.value}")
   


result=Array('i',4)
sum_total=Value('i')
list1=[1,2,3,4]
p1=multiprocessing.Process(target=square_list,args=(list1,result,sum_total))


p1.start()
p1.join()


print(sum_total.value)

for i in result:
    print(i)
