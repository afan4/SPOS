'''import threading
import time
import random

# Number of philosophers
num_philosophers = 5

# Forks (each fork is represented by a mutex)
forks = [threading.Lock() for _ in range(num_philosophers)]

# Philosopher function
def philosopher(id):
    left_fork = id  # Fork to the left
    right_fork = (id + 1) % num_philosophers  # Fork to the right

    while True:
        # Think (simulating time spent thinking)
        print(f"Philosopher {id} is thinking.")
        time.sleep(random.uniform(1, 3))

        # Pick up forks: first try to acquire the left fork, then the right fork
        with forks[left_fork]:
            print(f"Philosopher {id} picked up left fork.")
            with forks[right_fork]:
                print(f"Philosopher {id} picked up right fork.")
                # Eat (simulating time spent eating)
                print(f"Philosopher {id} is eating.")
                time.sleep(random.uniform(1, 3))
                print(f"Philosopher {id} finished eating.")
            
            # Put down forks after eating
            print(f"Philosopher {id} put down right fork.")
        print(f"Philosopher {id} put down left fork.")
        # Now philosopher goes back to thinking

# Create philosopher threads
philosophers = []
for i in range(num_philosophers):
    philosopher_thread = threading.Thread(target=philosopher, args=(i,))
    philosophers.append(philosopher_thread)

# Start all philosopher threads
for p in philosophers:
    p.start()

# Let philosophers run for some time before stopping the program
time.sleep(10)  # Run for 10 seconds
'''

'''import time
import threading
import random

num = 5
forks = [threading.Lock() for a in range(num)]

def philosopher(id):
    left=id-1
    right= (id+1) % num
    while True:
        print(f"P{id} is thinking")
        time.sleep(random.uniform(1, 3))
        with forks[left]:
            print(f"\tP{id} picked Left fork {left}")
            with forks[right]:
                print(f"\tP{id} picked Right fork {right}")
                print(f"\tP{id} is eating")
                time.sleep(random.uniform(1, 3))
            print(f"\tP{id} put down forks")


phils = []
for i in range(num):
    p=threading.Thread(target=philosopher, args=(i,))
    phils.append(p)

for p in phils:
    p.start()

time.sleep(10)
exit()


'''
        
import time
import threading
import random

num = 5
forks = [threading.Lock() for a in range(num)]

def philosopher(id):
    left = id 
    right = (id +1) % num
    while True:
        print(f"\tP{id} is thinking")
        time.sleep(random.uniform(1,3))
        with forks[left]:
            print(f"phil{id} picked left fork {left}")
            with forks[right]:
                print(f"phil{id} picked right fork {right}")
                print(f"\nphil{id} is now eating...\n")
                time.sleep(5)
            print(f"\nphil{id} kept down the forks {left}, {right}  \n")

phils =[]
for i in range(num):
    p = threading.Thread(target=philosopher, args=(i,))
    phils.append(p)
    p.start()


