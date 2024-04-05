import threading

def function1():
    for x in range(1000000):
        print("ONE")
def function2():
    for x in range(1000000):
        print("TWO")

thread1 = threading.Thread(target = function1)
thread2 = threading.Thread(target = function2)

thread1.start()
thread2.start()

#threadler sayesinde 2 ayrı fonksiyon aynı anda çalıştırılır