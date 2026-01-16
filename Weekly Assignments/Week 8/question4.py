import sys

if len(sys.argv) < 2:
    print("Error: No file provided")
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        text = file.read()
        lines = text.count("\n")
        chars = len(text)

    print("Lines:", lines)
    print("Characters:", chars)
except FileNotFoundError:
    print("Error: File not found")
