# opens file with name of "input_1.txt"
try:
    file = open("input_1.txt", "r")
except IOError:
    print("File not found or path is incorrect")

total = 0
for line in file:
    total += int(line)

file.close()

print(total)
