import multiprocessing
# print(multiprocessing.cpu_count())
from multiprocessing import Process

class SqProcess(Process):

    def __init__(self,num):
        self.num = num
        super().__init__()

    def run(self):
        return "square value of number is {}".format(self.num**2)


ps=SqProcess(5)
ps.start()
ps.join()
