# Assignment 4

This folder contains Python exercises demonstrating file handling operations.

## Tasks

### Task 1: File Reader with Error Handling (`task1.py`)
A program that reads and displays the content of a text file with proper error handling.

**Features:**
- Checks if the file exists before attempting to read it
- Reads `sample.txt` line by line
- Displays each line with line numbers
- Shows an error message if the file is not found

**Usage:**
```bash
python task1.py
```

**Example Output:**
```
Reading file content:
Line 1: This is sample text file.
Line 2: It containes multiple file.
```

**Error Handling:**
If the file doesn't exist:
```
Error: The file 'sample.txt' was not found.
```

### Task 2: File Write, Append, and Read (`task2.py`)
A program that demonstrates writing, appending, and reading file operations.

**Features:**
- Takes user input and writes it to `output.txt`
- Appends additional user input to the same file
- Reads and displays the final content of the file
- Demonstrates different file modes: 'w' (write), 'a' (append), 'r' (read)

**Usage:**
```bash
python task2.py
```

**Example Output:**
```
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
```

## Requirements
- Python 3.x
- os module (built-in)

## Files
- `task1.py` - File reading with error handling
- `task2.py` - File writing, appending, and reading
- `sample.txt` - Sample input file for task1
- `output.txt` - Generated output file from task2

## How to Run
Navigate to the assign-4 directory and run any task:
```bash
cd d:\tutedude\assignment\assign-4
python task1.py
# or
python task2.py
```

## Concepts Covered
- File reading and writing
- File modes ('r', 'w', 'a')
- Context managers (with statement)
- File existence checking using `os.path.exists()`
- Error handling for file operations
- Line-by-line file reading
- User input for file operations
