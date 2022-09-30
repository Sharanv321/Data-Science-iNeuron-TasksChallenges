# Q23) write a function which will be able to shutdonw your system .

# Create a function for shutdown
def shutdown():
    import os

    shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")

    if shutdown == 'no':
        exit()

    else:
        os.system("shutdown /s /t 1")

shutdown()
