import threading
import random
import time

db =0
mutex = threading.Lock()

def writer():
    while True:
        with mutex:
            global db
            db = random.randint(1,100)
            print("\n\nWriting to DB ", db)
        print("Writing complete...\n")
        time.sleep(random.randint(2,5))

def reader():
    while True:
        with mutex:
            global db
            print("Reading DB ", db)    
        time.sleep(1)

w = threading.Thread(target=writer)
r1 = threading.Thread(target=reader)

w.start()
r1.start()