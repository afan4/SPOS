'''
empty tracks how many empty.
full...
Producer looks at empty. If empty=0, wait. else dec empty. ek use ho gaya hai.

'''


import threading
import time
import random

buffer_size= 5
buffer = []

mutex= threading.Lock()
empty= threading.Semaphore(buffer_size)
full = threading.Semaphore(0)

def producer():
    while True:
        empty.acquire() #dec empty. if 0 wait
        mutex.acquire()
        item = random.randint(100,200)
        buffer.append(item)
        print(f"\nProduced item {item}. Buffer: ", buffer)
        mutex.release()
        full.release()
        time.sleep(random.uniform(0.1, 1))

def consumer():
    while True:
        full.acquire() #dec full. if 0, wait.
        mutex.acquire()
        i= buffer.pop(0)
        print(f"Consumed item {i}. Buffer: ", buffer)
        mutex.release()
        empty.release()
        time.sleep(random.uniform(0.1, 1))

pthread = threading.Thread(target=producer)
cthread = threading.Thread(target=consumer)

pthread.start()
cthread.start()

time.sleep(5)
exit()
