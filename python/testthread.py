import threading
import time

# def func1():
#     for x in range(50):
#         print("Hello")

# # def func2():
# #     for x in range(1000):
# #         print("TWO")

# t1 = threading.Thread(target=func1)
# # t2 = threading.Thread(target=func2)

# t1.start()
# # t2.start()

# t1.join()

# print("Tapos na")

# x = 8192

# lock = threading.Lock()

# def double():
#     global x, lock
#     lock.acquire()
#     while x <  16384:
#         x *= 2
#         print(x)
#         time.sleep(1)
#     print ("Reached The Max")
#     lock.release()

# def halve():
#     global x, lock
#     lock.acquire()
#     while x > 1:
#         x /= 2
#         print(x)
#         time.sleep(1)
#     print("Reached the minimum")
#     lock.release()

# t1 = threading.Thread(target=halve)
# t2 = threading.Thread(target=double)

# t1.start()
# t2.start()

# semaphore = threading.BoundedSemaphore(value=5)

# def access(thread_number):
#     print(f"{thread_number} is trying to access")
#     semaphore.acquire()
#     print(f"{thread_number} was granted access")
#     time.sleep(10)
#     print(f"{thread_number} is now releasing")
#     semaphore.release()

# for thread_number in range(1, 11):
#     t = threading.Thread(target=access, args=(thread_number,))
#     t.start()
#     time.sleep(1)


# event = threading.Event()

# def myfunction():
#     print("Waiting for event to trigger...")
#     event.wait()
#     print("WOOOOOOW")

# t1 = threading.Thread(target=myfunction)
# t1.start()

# x = input("y/n: ")
# if x == "y":
#     event.set()


path = "text.txt"
text = ""

def readTxt():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        time.sleep(3)

def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readTxt, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()