# Q6) Define a function for all the above problem statememnt

# Function to remove vowels
def removevowels(stringtext):
    s2 = ''
    for i in stringtext:
        if i not in ('a', 'e', 'i', 'o', 'u'):
            s2 = s2 + i
    print(s2)


removevowels("Try to filter out all the vowels form below text by using while loop : Python is dynamically-typed and "
             "garbage-collected.")


# function to print numbers not divisible by 3
def printnodivisibleby3(num1, num2):
    i = num1 + 1
    while i > num1 and i < num2:
        if i % 3 == 0:
            print(i)
        i += 1


printnodivisibleby3(40, 400)


# Function to get even numbers
def getevennumbers(num1, num2):
    i = 2
    while i > num1 and i < num2:
        if i % 2 == 0:
            print(i)
        i += 2


getevennumbers(1, 1000)
