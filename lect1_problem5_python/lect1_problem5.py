import numpy as np
import time

a = np.random.randint(1,700,100000)
b = np.random.randint(1,700,100000)
c = 0

print("=================================================================")
print("                  Slide 12                                       ")
print("=================================================================")


# For Loop
st = time.time()
for i in range(0, len(a)):
    c = c + a[i] * b[i]
et = time.time()
for_loop_time = et - st
print("For loop Sum: " , c)

# Dot Product
start = time.time()
c = a.dot(b)
end = time.time()
dot_product_time = end - start
print("Dot Product Sum: " , c)

# Division by zero exclusion
if for_loop_time == 0:
    speedup = "Negligible exec time using for loop"
elif dot_product_time == 0:
    speedup = "Negligible exec time using dot product library"
else:
    speedup = for_loop_time/dot_product_time

# Print Stats
print("For loop time: ",for_loop_time)
print("Dot Product time: ",dot_product_time)
print("Speedup: ", speedup)

# slide 13
print("=================================================================")
print("                            Slide 13                             ")
print("=================================================================")
n = 10000
a = np.random.randint(4,size=(n, n))
x = np.random.randint(1,4,n)

start = time.time()
result = [] 
for i in range(len(a)):
    row = []
    product = 0 
    for v in range(len(a[i])):
        product += a[i][v] * x[v]
    row.append(product)
        
    result.append(row)

end = time.time()

for_loop_time = end - start
print("For loop Sum: " , result[:4], "....")

start = time.time()
z = np.dot(a, x)
end = time.time()
print("For loop Dot Product: " , z[:4], "....")
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

n = 1000
a = np.random.randint(4,size=(n, n))
b = np.random.randint(4,size=(n, n))
result = [] 

start = time.time()
for i in range(len(a)):
    row = [] 
    for j in range(len(b[0])):
        
        product = 0 # the new element in the new row
        for v in range(len(a[i])):
            product += b[i][v] * b[v][j]
        row.append(product) # append sum of product into the new row
        
    result.append(row) # append the new row into the final result
end = time.time()

for_loop_time = end - start
print("For loop Sum: " , result[:1], "....")

start = time.time()
z = np.multiply(a,b) 
end = time.time()
print("Matrix Product Mul: " , z[:1], ".....")
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

def for_loop_nbyn():
    n = 1000
    a = np.random.randint(4,size=(n, n))
    b = np.random.randint(4,size=(n, n))
    result = [] 

    start = time.time()
    for i in range(len(a)):

        row = [] 
        for j in range(len(b[0])):
            
            product = 0 # the new element in the new row
            for v in range(len(a[i])):
                product += b[i][v] * b[v][j]
            row.append(product) # append sum of product into the new row
            
        result.append(row) # append the new row into the final result
    end = time.time()


