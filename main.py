#!/usr/bin/python3
from src.number_parser import check_number


def run():
    while True:
        value = input("Write number to check integer part or 'exit' to finish: \n")
        if value == "exit":
            break
        try:
            value = float(value)
        except ValueError:
            print("Only integer or float possible!!!")
            continue
        print(f"(in={value}, out={check_number(value)})")


if __name__ == '__main__':
    run()
