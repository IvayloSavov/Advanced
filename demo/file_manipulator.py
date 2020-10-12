import os

while True:
    line = input()
    if line == "End":
        break
    command, *args = line.split("-")

    if command == "Create":
        file_name = args[0]
        with open(file_name, "w") as file:
            file.write("")

    elif command == "Add":
        file_name, content = args[0], args[1]
        with open(file_name, "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        file_name, old_string, new_string = args[0], args[1], args[2]
        try:
            with open(file_name, "r") as file:
                text = file.read()
                text = text.replace(old_string, new_string)
            with open(file_name, "w") as file:
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        file_name = args[0]
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")