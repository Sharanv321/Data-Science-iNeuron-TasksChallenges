# Q17) write a function whihc will take multiple list as a input and give me concatnation of all the element as and output

# creating a function to concaternate
def concatenatelist(l1=[], l2=[]):
    for i in l2:
        l1.append(i)
    # Printing concatenated list
    print("Concatenated list : ", l1)


# Calling the function to concatenate
concatenatelist([2,5,7],[1,8,9,15])

