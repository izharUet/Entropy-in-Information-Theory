from collections import Counter
import math

# Given DNA sequence
sequence = (
    "ATGCTTAAGCTGCTTAACCTGAAGCTTCCGCTGAAGAACCTG"
    "CTGAACCCGCTTAAGCTGAACCTTCTGAAGCTTAACCTGCTT"
)
# Function to calculate entropy
def calculate_entropy(probabilities,order):
    entropy = 0
    for p in probabilities:
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy/order
# Function to calculate probabilities of symbols of a given order (n)
def calculate_probabilities(sequence, order):
    # Extract patterns of length 'order'
    pattern = [sequence[i:i + order] for i in range(len(sequence) - order + 1)]
    print(pattern)
    # Count occurrences of each pattern
    count_npattern = Counter(pattern)
    # Calculate probabilities
    total = len(pattern)
    probabilities = [count / total for item, count in count_npattern.items()]
    return probabilities

# Calculate entropy for first, second, third, and fourth order
for order in range(1, 5):
    probabilities = calculate_probabilities(sequence, order)
    entropy = calculate_entropy(probabilities,order)
    print(f"{order}-order entropy: {entropy:.4f} bits")
