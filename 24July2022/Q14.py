# Q14) you have to write a function which will take string and return a len of it without using a inbuilt fun len

# Creating a function to count the characters in the text
def StringLength(text):
    count = 0
    for i in text:
        count = count + 1

    print(count)

# Creating a function to print the count of the characters in the text
StringLength("aaabbbccc")