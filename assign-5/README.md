# Assignment 5: Data Structures and Strings in Python

This folder contains Python exercises demonstrating dictionaries, lists, and data manipulation.

## Tasks

### Task 1: Create a Dictionary of Student Marks (`task1.py`)
A program that manages student marks using a dictionary data structure.

**Features:**
- Creates a dictionary where student names are keys and marks are values
- Takes user input for a student's name
- Retrieves and displays the corresponding marks
- Handles cases where the student is not found

**Usage:**
```bash
python task1.py
```

**Example Output:**

If the student exists:
```
Enter the student's name: Alice
Alice's marks: 85
```

If the student does not exist:
```
Enter the student's name: John
Student not found.
```

**Predefined Students:**
- Alice: 85
- Bob: 92
- Charlie: 78
- Diana: 95
- Eve: 88

### Task 2: List Operations - Extract and Reverse (`task2.py`)
A program that demonstrates list slicing and reversal operations.

**Features:**
- Creates a list of numbers from 1 to 10
- Extracts the first five elements using slicing
- Reverses the extracted elements
- Displays both the extracted list and reversed list

**Usage:**
```bash
python task2.py
```

**Output:**
```
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
```

## Requirements
- Python 3.x

## How to Run
Navigate to the assign-5 directory and run any task:
```bash
cd d:\tutedude\assignment\assign-5
python task1.py
# or
python task2.py
```

## Concepts Covered
- **Dictionaries**: Key-value pairs, dictionary lookup, membership testing
- **Lists**: List creation, slicing, reversal
- **User Input**: Taking and processing user input
- **Conditional Statements**: if-else for error handling
- **Data Structures**: Working with Python's built-in data structures
- **List Operations**: `range()`, slicing `[:5]`, reversal `[::-1]`

## Learning Objectives
- Understand how to use dictionaries for data storage and retrieval
- Master list slicing and indexing techniques
- Learn to handle user input and edge cases
- Practice working with Python's built-in data structures
