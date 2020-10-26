def get_repeating_DNA(text):
    result = []
    for idx in range(0, len(text) - 10):
        current = text[idx:idx+10]
        next = text[idx+1:]
        if current in text[idx+1:] and current not in result:
            result.append(current)
    return result


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)


