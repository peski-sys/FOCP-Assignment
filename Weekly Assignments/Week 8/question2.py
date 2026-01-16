import sys

if len(sys.argv) < 3:
    print("Error: Two file names required")
    sys.exit()

file1, file2 = sys.argv[1], sys.argv[2]

try:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        if f1.read() == f2.read():
            print("Files are identical")
        else:
            print("Files are different")
except FileNotFoundError:
    print("Error: One or both files not found")
