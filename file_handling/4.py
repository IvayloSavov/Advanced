import os

try:
    os.remove("my_first_file.txt")
    print("Successfully deleted!")
except FileNotFoundError:
    print("File already deleted!")


####################
path = "my_first_file.txt"
if os.path.exists(path):
    os.remove(path)
    print("Successfully deleted!")
else:
    print("File already deleted!")

