# Write a python code to print the below pattern

# Creating a function to print the pattern
def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("")

# Calling the function to print the pattern
pattern(10)