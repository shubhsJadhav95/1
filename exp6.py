import threading
import time

sem = threading.Semaphore(1)  # only 1 thread allowed

def task(name):
    sem.acquire()
    print(f"{name} entering critical section")
    time.sleep(1)
    print(f"{name} leaving critical section")
    sem.release()

t1 = threading.Thread(target=task, args=("T1",))
t2 = threading.Thread(target=task, args=("T2",))

t1.start()
t2.start()

t1.join()
t2.join()