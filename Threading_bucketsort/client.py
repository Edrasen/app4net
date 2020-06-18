import socket
import pickle
import threading
import sys
import random
import functools
import reliable
import time
import quickLast

def server(HOST, PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print("waiting accept")
    conn, addr = s.accept()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("waiting for receive")
    myobject = pickle.loads(reliable.receive(conn))
    quickLast.quickSort(myobject, 0, len(myobject)-1)
    reliable.send(conn, myobject)
    conn.close

def argmin(values):             
    '''it helps to check minimum value on the list and return it's index"'''
    return min(range(len(values)), key=values.__getitem__)

def merge(src_list):
    '''src_list is a list of lists, each list is already sorted'''
    result = []
    while src_list:
        first = list(map(lambda a: a[0], src_list))         #creating a list of all first elements 
        min_indx = argmin(first)
        '''since we are working with a list of lists, using argmax function we are able to 
        work with the list which is being referenced by min_index, making all the append and 
        pop operations possible'''
        arr = src_list[min_indx]                            #get a reference to the list
        result.append(arr[0])
        arr.pop(0)
        if not arr:
            src_list.pop(min_indx)
    return result

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

def client(HOST, PORT, arr, result, i):
    '''it send to the server a partition of the original list'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    reliable.send(s, arr)
    res = pickle.loads(reliable.receive(s))
    #print(res)
    result[i] = res
    s.close()

n_threads = int(input("How many buckets do you want to use? "))
result_array = [None] * n_threads       #it creates a list of n elemens of none it helps to save all buckets array
rand_arr = [random.randint(0, 999) for i in range(3500)]        #it creates an array with 3500 random elements

partition = list(chunks(rand_arr, int(len(rand_arr) / n_threads)))  

HOST = "localhost"
PORT = 50007

# start the servers for listening the requests
servers = [threading.Thread(target=server, args=(HOST, PORT + i)) for i in range(n_threads)]
for t in servers: t.start()

clients = [threading.Thread(target=client, args=(HOST, PORT + i, partition[i], result_array, i)) 
        for i in range(n_threads)]
for t in clients: t.start()
for t in clients: t.join()
sorted_arr = merge(result_array)
print(sorted_arr)

for t in servers: t.join()

