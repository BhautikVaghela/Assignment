# Tkinter Calculator

A modern, fully functional calculator application built with Python's Tkinter library.

## Description

This is a graphical user interface (GUI) calculator that performs basic arithmetic operations. It features a clean, color-coded interface with error handling and support for decimal calculations.

## Features

- **Basic Arithmetic Operations**
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
  - Modulo (%)

- **User-Friendly Interface**
  - Clear display with large font
  - Color-coded buttons for easy identification
  - Responsive button layout

- **Additional Functions**
  - Clear (C) - Resets the calculator
  - Backspace (⌫) - Deletes the last character
  - Decimal point support
  - Error handling for invalid expressions

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Ensure Python is installed on your system
2. Clone or download this repository
3. No additional packages required - Tkinter comes with Python

## How to Run

```bash
python task1.py
```

Or simply double-click the `task1.py` file if you have Python configured to run .py files.

## Usage

1. **Input Numbers**: Click on the number buttons (0-9)
2. **Perform Operations**: Click on operation buttons (+, -, *, /, %)
3. **Calculate Result**: Press the equals (=) button
4. **Clear Display**: Press the C button to clear everything
5. **Delete Character**: Press the ⌫ button to remove the last character
6. **Decimal Numbers**: Click the decimal point (.) button for floating-point numbers

### Example Calculations

- Basic addition: `5 + 3 = 8`
- Decimal operations: `10.5 * 2 = 21.0`
- Complex expressions: `(15 + 5) * 2` (type: `15+5)*2` and press =)

## Interface

The calculator features a modern design with:

- **Blue buttons**: Numbers (0-9)
- **Red buttons**: Operators (+, -, *, /, %)
- **Gray buttons**: Special functions (C, ⌫)
- **Green button**: Equals (=)
- **Dark theme**: Professional appearance with contrasting colors

## Code Structure

- `press(num)`: Adds numbers/operators to the expression
- `equalpress()`: Evaluates the mathematical expression
- `clear()`: Clears the display
- `backspace()`: Removes the last character
- Grid layout for organized button placement

## Error Handling

The calculator includes error handling for:
- Division by zero
- Invalid mathematical expressions
- Syntax errors

When an error occurs, "Error" is displayed, and the calculator resets for the next calculation.

## Window Specifications

- **Size**: 400x550 pixels
- **Fixed window**: Non-resizable for consistent UI
- **Background**: Dark theme (#2C3E50)
- **Display**: Large, easy-to-read entry field

## Future Enhancements

Potential improvements could include:
- Scientific calculator functions (sin, cos, tan, etc.)
- Memory functions (M+, M-, MR, MC)
- Keyboard input support
- Calculation history
- Theme customization

## License

Free to use and modify for educational purposes.

## Author

Created as part of Assignment 6

---

**Note**: This calculator uses Python's `eval()` function for expression evaluation. In production applications, consider using safer alternatives like `ast.literal_eval()` or a custom expression parser.
