import time

def timeconsuming():
    time.sleep(5)
    return

n = 3
start = time.time()
for i in range(0, n):
    timeconsuming()
end = time.time()
dot_product_time = end - start
print("Excecution: " , dot_product_time)

