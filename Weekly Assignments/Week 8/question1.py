import sys

if len(sys.argv) < 2:
    print("Error: No file provided")
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        for i, line in enumerate(file, start=1):
            print(f"{i}\t{line.rstrip()}")
except FileNotFoundError:
    print("Error: File not found")
