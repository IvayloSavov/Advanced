def get_repeating_DNA(sequence):
    repeating_sequences = []
    for i in range(len(sequence) - 10):
        current_sequence = sequence[i:i+10]
        if len(current_sequence) == 10:
            for j in range(i + 1, i + 11):
                next_sequence = sequence[j:j+10]
                if next_sequence == current_sequence and current_sequence not in repeating_sequences:
                    repeating_sequences.append(current_sequence)
                    break
    return list(repeating_sequences)