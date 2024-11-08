'''
Code By Afan Shaikh. It's 2.04 AM...

SJF is preemptive as per syllabus. 
quan is Time quantum for RR
self.rt = remaining time
cp = current process
Our table is just a list of process objects
'''
class Process:
    def __init__(self):                             
        self.name =input("Enter Process Name: ")
        self.at = int(input("Enter Arrival Time: "))
        self.bt = int(input("Enter Burst Time: "))
        self.pr = int(input("Enter Priority: "))
        self.wt = 0
        self.tat =0
        self.ct = 0
        self.rt = self.bt #remaining time
    def display(self):
        print(f"{self.name}:\t{self.at}\t{self.bt}\t{self.wt}\t{self.ct}\t\t{self.tat}\n")

table =[]
while True:
    ch=int(input("\nAdd a new process?"))
    if ch:
        p = Process()
        table.append(p)
    else: break

def fcfs():
    time=0
    table1= sorted(table, key= lambda p: p.at)
    for p in table1:
        p.wt=time-p.at
        p.ct=time+p.bt
        p.tat=p.wt+p.bt
        time += p.bt
    print("\n\n\nFCFS:")
    printer(table1)

def sjf():
    res = []
    table1= sorted(table, key= lambda p: p.at)
    cp = table1[0] 
    time =0
    print(f"\nStarting with first: {cp.name}")
    while True:
        for a in table1:
            if a.at<=time and a.rt < cp.rt:
                print(f"\nHalting {cp.name} {cp.rt} \nStarting {a.name} remaining time: {a.rt}")
                cp=a
                break
        time+=1
        print(f"Time: {time}")
        cp.rt-=1
        if not cp.rt:
            cp.ct= time
            cp.tat= time-cp.at
            res.append(cp)
            table1.remove(cp)
            if not table1: break
            min=table1[0]
            for a in table1:
                if a.at<=time and a.rt< min.rt:
                    min = a
            print(f"\nCompleted {cp.name}\nStarting {min.name} remaining time: {min.rt}")
            cp=min
            cp.wt=time-cp.at
        

    print("\n\nSJF:")
    printer(res)

def priority():
    time=0
    table1= sorted(table, key= lambda p: p.pr)
    for p in table1:
        p.wt=time-p.at
        p.ct=time+p.bt
        p.tat=p.wt+p.bt
        time += p.bt
    print("\n\n\nPRIORITY:")
    printer(table1)

def robin():
    quan= 5
    time =0
    queue= sorted(table, key= lambda p: p.at)
    res = []
    cp= queue[0]
    i=0
    while True:
        if len(queue)==len(res): break
        i+=1
        print(f"\n\nRound {i} Time: {time}")
        for cp in queue:
            if cp not in res:
                print(f"{cp.name} {cp.rt}")
                cp.rt-= quan
                if cp.rt<=0: 
                    time+= quan+cp.rt
                    print(f"\tCompleted {cp.name} at Time: {time}")
                    cp.tat= time-cp.at
                    cp.ct= time
                    res.append(cp)
                else: time += quan
    print("\n\nRound Robin:")
    printer(res)

def printer(list):
    i=0
    for a in list:
        i+=1
        print(f"{i}.  {a.name}\t{a.at}\t{a.bt}\t{a.wt}\t{a.ct}")

printer(table)

#Code By Afan Shaikh. It's 2.04 AM...
#fcfs()
sjf()
#priority()
#robin()