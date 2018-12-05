# file_util.py
def read_file_return_lines(file_name):
    try:
        file = open(file_name, "r")
    except IOError:
        print("File not found or path is incorrect")
        return []

    lines = [line for line in file.read().splitlines()]

    file.close()

    return lines
