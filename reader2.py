import time
import random
import threading

#reader writer problem

db = 0

mutex = threading.Lock()

def writer():
    while True:
        global db
        print('\nwriter waits for access')
        mutex.acquire()
        print('writer has access now')
        db = random.randint(1,10)
        print(f'writer writes DB: {db}\n\n')
        mutex.release()
        time.sleep(1)

def reader(id):
    while True:
        global db
        print(f'\nR{id} waits for access')
        mutex.acquire()
        print(f'R{id} reads DB: {db}')
        mutex.release()
        time.sleep(random.uniform(3,5))

threading.Thread(target=writer).start()

readers = []
for i in range(3):
    readers.append(threading.Thread(target=reader, args=(i,)))
    readers[i].start()

