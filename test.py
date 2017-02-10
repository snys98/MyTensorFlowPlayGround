# encoding:utf-8
"""This is a testrunner file."""

import demo.examples


def main():
    """entrance method"""

    available_demos = [x for x in demo.examples.__dict__.values() if isinstance(
        x, type) and demo.examples.DemoBase in x.__bases__]
    print("Please select the demo to run: \n")
    index = 1
    for each_demo in available_demos:
        print("%d. %s" % (index, each_demo.__name__))
        index += 1
    key_input = input("")
    input_value = int(key_input)
    if input_value >= 0 and input_value < len(available_demos):
        getattr(demo.examples, available_demos[input_value].__name__).run()
    else:
        print("Program ended")
    return

if __name__ == '__main__':
    main()
