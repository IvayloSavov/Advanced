def find_symbol(words, symbol):
    for i in range(len(words)):
        word = words[i]
        if symbol in word:
            return i, word.index(symbol)

    return None


n = int(input())
words = [input() for _ in range(n)]
symbol = input()

if find_symbol(words, symbol):
    print(find_symbol(words, symbol))
else:
    print(f"{symbol} does not occur in the matrix")