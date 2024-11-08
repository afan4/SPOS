#producer consumer problem

import time
import random
import threading

empty = threading.Semaphore(5)
full = threading.Semaphore(0)
mutex = threading.Lock()

buffer=[]
num = 5

def producer():
    while True:
        print("\nproducer waits for slot")
        empty.acquire()
        print("found a slot")
        mutex.acquire()
        item = random.randint(101, 199)
        buffer.append(item)
        print(f"Produced item: {item}\n Buffer: {buffer}")
        full.release()
        time.sleep(1)
        mutex.release()
        time.sleep(random.randint(1,1))
def consumer():
    while True:
        print("\nconsumer waits in queue")
        full.acquire()
        print("consumer will now consume")
        mutex.acquire()
        print(f"consumed item: {buffer.pop(0)}")
        empty.release()
        mutex.release()
        time.sleep(random.randint(3,5))

threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()
time.sleep(10)

