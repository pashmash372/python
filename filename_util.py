import sys


def remove_spaces_and_replace_colon_with_hyphen(string):
    print("String before processing: ", string)
    return string.replace(" ", "").replace(":", "-") + ".ipynb"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python remove_spaces_and_replace_colon_with_hyphen.py <input_string>")
    else:
        input_string = "".join(sys.argv[1::])
        print(remove_spaces_and_replace_colon_with_hyphen(input_string))
