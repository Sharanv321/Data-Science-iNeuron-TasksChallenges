# Q3) Try to print all the number divisible by 3 in between a range of 40 - 400

# Using a while loop to print all the number divisible by 3 in between a range of 40 - 400
i = 41
while i >40 and i < 400:
    if i % 3 == 0:
        print(i)
    i+= 1