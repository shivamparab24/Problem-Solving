# Create a countdown timer that starts from a given number and counts down to zero using a while loop.


import time

count = int(input("Enter the countdown: "))

while count > 0:
    print(count)
    time.sleep(1) #used to add delay
    count = count - 1

print("Blast Off...")