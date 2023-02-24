import random


def randomString():
    letters = [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(995)]
    pos = random.randint(0, 994)
    letters = letters[:pos] + ["A", "B", "C", "B", "A"] + letters[pos:]
    return "".join(letters)

for i in range(1, 101):
    file = open(str(i) + ".txt", "w")
    randomTxt = randomString()
    a = file.write(randomTxt)
    file.close()
    print(a)
