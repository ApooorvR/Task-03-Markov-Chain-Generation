import random
from collections import defaultdict

# Load text
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

# Tokenize
words = text.split()

# Build Markov Chain
markov_chain = defaultdict(list)

for i in range(len(words) - 1):
    markov_chain[words[i]].append(words[i + 1])

def generate_text(start_word, length=20):
    if start_word not in markov_chain:
        return f"'{start_word}' has no transitions in training data."

    current_word = start_word
    result = [current_word]

    for _ in range(length):
        next_words = markov_chain[current_word]
        if not next_words:
            break
        current_word = random.choice(next_words)
        result.append(current_word)

    return " ".join(result)

# ---- USER INPUT ----
start_word = input("Enter a starting word: ").lower()

print("\nGenerated Text:\n")
print(generate_text(start_word))
