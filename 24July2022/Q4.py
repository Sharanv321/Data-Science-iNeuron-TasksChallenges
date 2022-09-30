# Q4) Try to filter out all the vowels form below text by using while loop : """Python is a high-level, interpreted,
# general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant
# indentation.[32]

text = 'Try to filter out all the vowels form below text by using while loop : Python is dynamically-typed and ' \
       'garbage-collected. '

# Creating a for loop to read the entire text and remove vowels
s1 = ''
for i in text:
    if i not in ('a', 'e', 'i', 'o', 'u'):
        s1 = s1 + i

print(s1)