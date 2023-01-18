import threading, time

def func():
    print("Funzione Principale")
 
 
def endless_func():
    while True:
        print("Funzione Infinita")

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=endless_func)

t1.start()
t2.start()

t1.join()
t2.join()

print("Finito")