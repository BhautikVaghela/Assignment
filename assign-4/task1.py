import os 

filename = "sample.txt"

if os.path.exists(filename):
    print("Reading file content:")
    with open(filename, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, 1):
            print(f"Line {i}: {line.strip()}")
else:
    print(f"Error: The file '{filename}' was not found.")
