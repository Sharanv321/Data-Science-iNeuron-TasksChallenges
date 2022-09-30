# Q21) write a function which can help you to filter only word file from a directory .

import os

# Creating a function to list all word files which takes path as input parameter
def ListAllWordFiles(path):
    # use os.listdir to get the list of all the files
    for file in os.listdir(path):

        # check the files which are end with word file extention

        if file.endswith(".docx"):
            # print path name of files
            print(os.path.join(path, file))

# Calling the function with passing the path as parameter
ListAllWordFiles("C://Users//shara//Desktop//Javascript")

