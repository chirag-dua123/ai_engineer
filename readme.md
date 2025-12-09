
# Project Structure

This repository contains basic Python utilities and learning examples.

## Files

### `basics.py`
Introduction to fundamental Python concepts including:
- Variables and data types
- Control flow (if/else, loops)
- Functions and scope
- Lists, dictionaries, and tuples
- String manipulation

### `calculator.py`
A simple command-line calculator supporting:
- Addition, subtraction, multiplication, division
- Basic arithmetic operations
- User input validation

**Usage:**
```bash
python calculator.py
```

### `wordcount.py`
Analyzes text files and displays the 10 most frequently used words.

**Usage:**
```bash
python wordcount.py <filename>
```

**Output:** Prints word frequencies in descending order

## Installation

Install dependencies:
```bash
pip install -r requirements.txt
```

## Testing

Run tests from the `tests/` folder:
```bash
pytest tests/
```

## Project Layout
```
├── basics.py
├── calculator.py
├── wordcount.py
├── requirements.txt
└── tests/
```
