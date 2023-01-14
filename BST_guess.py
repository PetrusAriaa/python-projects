from random import randint
from time import sleep

MIN = 0
MAX = 10
number = randint(MIN, MAX)
print("Your number is", number)
sleep(1)

print("RUN SEARCHING...")
sleep(3)
a, b = MIN, MAX+1
counter = 0
while True:
    center = a + (abs(a-b)//2)
    sleep(0.1)
    print(center)
    if number == center:
        print("Found in",counter,"iteration(s)")
        break
    elif number > center:
        a = center
    else:
        b = center
    counter += 1

