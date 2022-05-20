## Task solution

### Challenge goal
Write a Python function that accepts "a number" and outputs the number of (base-10) digits needed to write the integer part of that number on a piece of paper. Here, "a number" is any Python type in the standard library that behaves as a number (including but not limited to `int` and `float`).

###Example input & output

(in=100, out=3), (in=999, out=3), (in=-10, out=2), (in=3.1415, out=1)

## Requirements
- Python 3.9
- Pytest
- Make
- Poetry

Prepare venv for your own, install poetry by `pip install poetry` then run `poetry install` and here you go.

## Run application
### by Makefile
`make run`
### by python command
`python main.py`

## Run tests
### by Makefile
`make test`
### by python command
`pytest -v`
