import re

line = input("Type : ")
res = re.search(r'\D',line).start()
op = line[res]
numbers = [int(x) for x in line.split(op)]

print({
    '+':numbers[0] + numbers[1],
    '-':numbers[0] - numbers[1],
    '*':numbers[0] * numbers[1],
    '/':numbers[0] / numbers[1],
}[op])
