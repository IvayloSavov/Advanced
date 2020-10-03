def concatenate(*args):
    string = ""
    for x in args:
        string += x

    return string


print(concatenate("Soft", "Uni", "Is", "Great", "!"))