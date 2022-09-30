# Q12) Write a code to check a perticular installation in your system

# import modules
import winapps

b = False

# get each application with list_installed()
for item in winapps.list_installed():
    print(item.name)
    print(item.version)
    print(item.install_date)
    print(item.install_location)
    print('\n')