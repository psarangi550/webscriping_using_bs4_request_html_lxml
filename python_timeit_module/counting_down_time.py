import timeit #importing the timeit module
import time  #importing the time module

#using the time.process_time as the timer in here to know the process_time

print(timeit.timeit(
"""
def func(num):
    if num % 5 ==0:
        return num

gen_obj=(i for i in range(100) if func(i) )
""",
    timer=time.process_time,
    number=1000
))

#using the time.process_time as the timer in here to know the overall_time which consider time.sleep()

print(timeit.timeit(
"""
def func(num):
    if num % 5 ==0:
        return num

gen_obj=(i for i in range(100) if func(i) )
""",
    timer=time.perf_counter,
    number=1000
))



