# Q19) write a function whihc will be able to read a image file and show it to you .

def ReadImageFile(path):
    # Python program to read image file using matplotlib

    # importing matplotlib modules
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt

    # Read Images
    img = mpimg.imread(path)

    # Output Images

    plt.imshow(img)
    ReadImageFile('C://Users//shara//Desktop//Javascript//image1.png')
    plt.show()