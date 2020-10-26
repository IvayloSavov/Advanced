def get_repeating_DNA(text):
    repeating_sequences = []
    for i in range(0, len(text) - 10):
        current_sequence = text[i:i + 10]
        if current_sequence in text[i + 1:] and current_sequence not in repeating_sequences:
            repeating_sequences.append(current_sequence)
    return repeating_sequences


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)
