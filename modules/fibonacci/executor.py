from . import create_sequence


class Executor:
    def __init__(self):
        self.sequence = [

        ]
    def run(self):
        while True:
            res = self.run_once()
            if not res:
                break


    def run_once(self):
        command = input()
        if command.startswith("Create Sequence "):
            n = int(command.split()[-1])
            self.__sequence = create_sequence(n)
            print(self.__sequence)
        elif command.startswith("Locates "):
            search = int(command.split()[-1])
            try:
                pos = sequence.index(search)
                print(f"The number - {search} is at index {pos}")
            except ValueError:
                print(f"The number {search} is not the sequence")
            except NameError:
                print("Make sure to create sequence first")
        elif command == "Stop":
            return False
        return True