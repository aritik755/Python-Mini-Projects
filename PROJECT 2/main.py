import random
n = random.randint(1, 100)
a = -1
gusses = 1
while(a != n) :
    a = int(input("Guess the Number: "))
    if(a > n):
        print("Lower Number Please")
        gusses += 1
    elif(a < n):
        print("Higher Number Please")
        gusses += 1

print(f"You the Gussed the correct number {n} in {gusses} attempts.")
    