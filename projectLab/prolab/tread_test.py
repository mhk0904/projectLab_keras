from threading import Thread

def work(result):
    total = 0
    for i in range(10):
        total += i
    result.append(total)
    #print("i'm thread 1")
    return

if __name__ == "__main__":
    result = list()
    th1 = Thread(target=work, args=(result))
   
    th1.start()
    th1.join()
    while(True):
        a = result.get() 
        print(a)

#print(f"Result: {sum(result)}")