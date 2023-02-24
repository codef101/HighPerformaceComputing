import time
import threading
import queue
import random
import multiprocessing

def timeconsuming():
    time.sleep(random.randint(1, 5))
    return

n = 40

start = time.time()
for i in range(0, n):
    timeconsuming()
end = time.time()
sequential_time = end - start
print("Sequential Time Elapsed: " , sequential_time)

q = queue.Queue()
for i in range(n):
    q.put(i)

def worker():
    while True:
        timeconsuming()
        q.task_done()

cpus = multiprocessing.cpu_count()
print("Creating %d threads" % cpus)
start = time.time()
for i in range(cpus):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

q.join()
end = time.time()

parallel_time = end - start

print("Parallel Time Elapsed: " , parallel_time)

# Stats
speedup = sequential_time/parallel_time
avg_efficiency = speedup/4
print("SpeedUp:" , speedup)
print("Average Efficiency:" , avg_efficiency)