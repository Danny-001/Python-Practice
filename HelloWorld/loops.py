# looping refers to the process of executing a block of code multiple times. Python provides two main types of loops: for loops and while loops.



#for loop - A for loop is used to iterate over a sequence (such as a list, tuple, string, or range).
#              used to execute a block of code fixed nuber of times.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for cabbage in fruits:
    print(cabbage)

for apple in fruits:
    print(apple)

vegetables = ["carrot", "broccoli", "spinach"]
for x in vegetables:
    print(x)

# You can also use range() to loop a specific number of times:

for i in range(5):
    print(i)

for missed_calls in range(3):
    print("You have a missed call.")

for sos in range(10):
    print("Help me!!!")

for countdown in range(5, 0, -1):
    print(countdown)




# while loop - A while loop continues to execute as long as a specified condition is true.

count = 3
while count < 5:
    print(count)
    count += 1  # Increment the counter to avoid infinite loop


players = 7
while players <= 11:
    print("The match is on!")
    players += 1


time = 10
while time > 5:
    print("The event starts in", time, "seconds")
    time -= 1