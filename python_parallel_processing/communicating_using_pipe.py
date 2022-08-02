from multiprocessing import Pipe
#importing the Pipe class from the multiprocessing module 
import multiprocessing #importing the multiprocessing module

list1=["Hi","Hello","Hru","END"]
#defining the list of messages 

def send_msg(list1,conn):
    for msg in list1: #iterating over the list
        conn.send(msg) #sending the messages 
    conn.close() #closing the messages

def recv_message(conn):
    while True:
        msg=conn.recv() #receiving the message
        #this is consoder one type of blocking like socket.recv()
        if msg=="END": #if the messages are END then
            break
        print(msg)

conn1,conn2=Pipe() #creating the connection which will be used in both the end 

ps1=multiprocessing.Process(target=send_msg,args=(list1,conn1))
ps2=multiprocessing.Process(target=recv_message,args=(conn2,))

ps1.start()
ps2.start()

ps1.join()
ps2.join()