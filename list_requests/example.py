import threading
import time
import random

print(f" Всё началось в {time.time()}")

spisok=["Петя","Костя","Коля","Наташа","Женя"]

key=0
start=0
finish=0
def target_func(name,b): # имитация реквеста
    global key,start,finish
    #time.sleep(1)
    b.wait()

    if key==0:
        start = time.time()
        print(start)
        key=1

    print (f"{name} молодец в {time.time()}")

#amount = random.randint(1, 15)
#print(amount)

#target_func(spisok[2])
def gonka():
    global finish
    running = []
    b = threading.Barrier(5, timeout=90)
    for name in spisok:
        thread = threading.Thread(target=target_func,args=(name,b,))
        time.sleep(random.randint(1, 10))
        thread.start()

        running.append(thread)


    for r in running:
        r.join()
    finish = time.time()
    total_time=(finish-start)
    print(total_time)




gonka()




