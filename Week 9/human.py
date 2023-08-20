import random

def generate_random_sequence(length):
    bases = ['A', 'T', 'G', 'C']
    random_sequence = ''.join(random.choice(bases) for _ in range(length))
    return random_sequence

sequence_length = 1000  # Change this to the desired length
random_dna_sequence = generate_random_sequence(sequence_length)

output_file = "human.txt"

with open(output_file, "w") as f:
    f.write(random_dna_sequence)

print(f"Random DNA sequence of length {sequence_length} has been written to {output_file}.")
