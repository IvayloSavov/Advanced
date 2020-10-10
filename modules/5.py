import fibonacci

while True:
    command = input()
    if command.startswith("Create Sequence "):
        n = int(command.split()[-1])
        sequence = fibonacci.create_sequence(n)
        print(sequence)
    elif command.startswith("Locate "):
        search = int(command.split()[-1])
        try:
            pos = sequence.index(search)
            print(f"The number - {search} is at index {pos}")
        except ValueError:
            print(f"The number {search} is not the sequence")
        except NameError:
            print("Make sure to create sequence first")
    elif command == "Stop":
        break
