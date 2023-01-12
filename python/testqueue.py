import queue

# q = queue.Queue()
# w = queue.LifoQueue()
e = queue.PriorityQueue()

# numbers = [10, 20, 30, 40, 50, 60, 70]
# for number in numbers:
    # q.put(number)
    # w.put(number)

# while True:
#     # print(q.get())
#     print(w.get())

e.put((2, "hello world"))
e.put((11, 99))
e.put((5, 7.5))
e.put((1, True))

while not e.empty():
    print(e.get())