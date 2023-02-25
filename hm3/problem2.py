import time
from multiprocessing import Pool
import os
import random

def randomString():
    letters = [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(995)]
    pos = random.randint(0, 994)
    letters = letters[:pos] + ["A", "B", "C", "B", "A"] + letters[pos:]
    return "".join(letters)

def file_generator():
    for i in range(1, 101):
        file = open(str(i) + ".txt", "w")
        randomTxt = randomString()
        a = file.write(randomTxt)
        file.close()

def has_five_letter_palindrome(string):
    for i in range(len(string)-4):
        substring = string[i:i+5]
        if substring == substring[::-1]:
            return True
    return False

def examine_strings(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            if has_five_letter_palindrome(string[i:j]):
                return True
    return False

def process_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    found = examine_strings(data)
    if found:
        return 1
    else:
        return 0

if __name__ == '__main__':

    
    count = 0
    start = time.time()
    for i in range(1, 101):
       count += process_file('palindrome_txts/{}.txt'.format(i))
    end = time.time()
    sequential_time = end - start

    print("Palindromes Found:" , count)
    print("Sequential Elapsed Time:" , sequential_time)

    start = time.time()
    pool = Pool(os.cpu_count())
    count = sum(pool.map(process_file, ['palindrome_txts/{}.txt'.format(i) for i in range(1, 101)]))
    end = time.time()
    parallel_time = end - start
    speedup = sequential_time/parallel_time

    print("Palindromes Found:", count)
    print("ParallelElapsed Time:", parallel_time)

    print("Speed Up: ", speedup)
    print("Efficiency : ", speedup/os.cpu_count())
