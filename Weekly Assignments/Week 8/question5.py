import sys
import string

if len(sys.argv) < 3:
    print("Error: File and dictionary required")
    sys.exit()

text_file = sys.argv[1]
dict_file = sys.argv[2]

try:
    with open(dict_file, "r") as d:
        dictionary = set(word.strip().lower() for word in d)

    with open(text_file, "r") as f:
        text = f.read().lower()

    # Remove punctuation
    for char in string.punctuation:
        text = text.replace(char, " ")

    words = text.split()

    misspelled = set()

    for word in words:
        if word not in dictionary:
            misspelled.add(word)

    for word in sorted(misspelled):
        print(word)

except FileNotFoundError:
    print("Error: File not found")
