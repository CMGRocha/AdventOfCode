# opens file with name of "input_1.txt"
try:
    file = open("input_1.txt", "r")
    # file = open("test_data.txt", "r")
except IOError:
    print("File not found or path is incorrect")

lines = [line for line in file.readlines()]

file.close()

current = 0
found = 0
previousFreq = set()
while found != 1:
    for line in lines:
        current += int(line)
        if current in previousFreq:
            found = 1
            break
        else:
            previousFreq.add(current)

print(current)
