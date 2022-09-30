# Q18) Write a function which will whould return list of all the file name from a directory .

# Creating  a function to get the directory list
def getthedirectorylist(path):
    import os

    # set the path of the directory
    directory_list = os.listdir(path)
    return directory_list

# Calling the function to print the directory
print(getthedirectorylist("C://Users//shara//Desktop//Javascript"))