def palindrome(*args):
    word = args[0]
    if word == word[::-1]:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"


print(palindrome("peter", 0))

