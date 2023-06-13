# Random number guessing game in python 

import random as rd 

start = int(input("Enter beginning value: "))
end = int(input("Enter ending value: "))


number = rd.randint(start, end + 1)

print("=======================================")
print("You have 10 chances to guess the number")
print("=======================================")

for i in range(1,10+1):
    ans = int(input("Enter your guess: "))
    if( ans == number ): 
        print()
        print("You have guess the number!")
        break
    else: 
        print("Wrong guess!")