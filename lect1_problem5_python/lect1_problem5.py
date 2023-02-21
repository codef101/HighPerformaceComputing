import numpy as np
import time

a = np.random.randint(1,500,10000)
b = np.random.randint(1,500,10000)
c = 0

print("=================================================================")
print("                  Slide 12                                       ")
print("=================================================================")
st = time.time()
c = sum([x*y for x,y in zip(a,b)])
et = time.time()
for_loop_time = et - st
print("For loop Sum: " , c)

start = time.time()
c = a.dot(b)
end = time.time()
print("Dot Product Sum: " , c)

dot_product_time = end - start

if for_loop_time == 0:
    speedup = "Negligible exec time using for loop"
elif dot_product_time == 0:
    speedup = "Negligible exec time using dot product library"
else:
    speedup = for_loop_time/dot_product_time

print("For loop time: ",for_loop_time)
print("Dot Product time: ",dot_product_time)
print("Speedup: ", speedup)

# slide 13
print("=================================================================")
print("                            Slide 13                             ")
print("=================================================================")
n = 1000000
a = [np.random.randint(1,1000000,n), np.random.randint(1,100000,n)]
x = np.random.randint(1,100000,n)

start = time.time()
sum = sum([x*y for x,y in zip(x,a)])
end = time.time()

for_loop_time = end - start
print("For loop Sum: " , sum)

start = time.time()
z = np.dot(a,x) 
end = time.time()
print("For loop Dot Product: " , sum)
dot_product_time = end - start

if for_loop_time == 0:
    speedup = "Negligible exec time using for loop"
elif dot_product_time == 0:
    speedup = "Negligible exec time using dot product library"
else:
    speedup = for_loop_time/dot_product_time

print("For loop time: ",for_loop_time)
print("Dot Product time: ",dot_product_time)
print("Speedup: ", speedup)

# slide 14
print("=================================================================")
print("                            Slide 14                           ")
print("=================================================================")
n = 4
a = [np.random.randint(1,1000000,n), np.random.randint(1,100000,n)]
b = [np.random.randint(1,1000000,n), np.random.randint(1,100000,n)]

start = time.time()
sum = sum([x*y for x,y in zip(b,a)])
end = time.time()

for_loop_time = end - start
print("For loop Sum: " , sum)

start = time.time()
z = np.cross(a,b) 
end = time.time()
print("For loop Dot Product: " , sum)
dot_product_time = end - start

if for_loop_time == 0:
    speedup = "Negligible exec time using for loop"
elif dot_product_time == 0:
    speedup = "Negligible exec time using dot product library"
else:
    speedup = for_loop_time/dot_product_time

print("For loop time: ",for_loop_time)
print("Dot Product time: ",dot_product_time)
print("Speedup: ", speedup)

print("=================================================================")
print("                            Slide 15                           ")
print("=================================================================")

