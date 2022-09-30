# Q24) Write a function which will whould return list of all the file name from a directory .

# Create a function to get the list of directory
def getthedirectorylist(path):
    import os

    # set the path of the directory

    directory_list = os.listdir(path)

    return directory_list

print(getthedirectorylist("C://Users//shara//Desktop//Javascript"))