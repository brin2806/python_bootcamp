# review exercise page 86 RealPython
from random import randint
# print (randint(1,6))
sum = 0
for throw in range(0, 10000):
    num = randint(1, 6)
    sum = sum + num

print("average = {}".format(sum/10000))
