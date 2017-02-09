# encoding:utf-8
"""This is a testrunner file."""

from demo import Demo

def main():
    """entrance method"""
    key_input = input("Please enter to start.")
    if key_input == '':
        instance = Demo()
        instance.run()
    else:
        print("Program ended")
    return

if __name__ == '__main__':
    main()
