import sys, os

# input and file stuff, it's boring
argv = sys.argv
argc = len(argv)

if argc < 2:
    print("Missing file argument...")
    quit()
elif argc > 3:
    print("Too many arguments...")
    quit()
else:
    f_in = argv[1]
    if argc == 3:
        f_out = argv[2]
    else:
        f_out = "out"

if not os.path.isfile(f_in):
    print("Assembly file does not exist...")
    quit()

with open(f_in) as f:
    text = f.readlines()

# first pass we'll get our labels, their names and addresses
class Label:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

labels = []
for i in range(0, len(text)):
    if text[i][0] == ".":
        labels.append(Label(text[i]), i * 3)

# now we can actually start translating our instructions
for i in range(0, len(text)):
    line = text[i].strip("\n").replace(",", "")
    line = line.split(" ")
    
    # kinda lame way to do this but it's easy to read/understand
    if line[0].lower() == "hlt":
        b = [0b0000, 0b0000, 0b0000, 0b0000]
    elif line[0].lower() == "add":
        rx, ry, rz = int(line[1][1:]), int(line[2][1:]), int(line[3][1:])
        b = [0b0001, rx, ry, rz]

    elif line[0].lower() == "sub":
        rx, ry, rz = int(line[1][1:]), int(line[2][1:]), int(line[3][1:])
        b = [0b0010, rx, ry, rz]

    elif line[0].lower() == "mul":
        rx, ry, rz = int(line[1][1:]), int(line[2][1:]), int(line[3][1:])
        b = [0b0011, rx, ry, rz]

    elif line[0].lower() == "and":
        rx, ry, rz = int(line[1][1:]), int(line[2][1:]), int(line[3][1:])
        b = [0b0100, rx, ry, rz]

    elif line[0].lower() == "or":
        rx, ry, rz = int(line[1][1:]), int(line[2][1:]), int(line[3][1:])
        b = [0b0101, rx, ry, rz]

    elif line[0].lower() == "xor":
        rx, ry, rz = int(line[1][1:]), int(line[2][1:]), int(line[3][1:])
        b = [0b0110, rx, ry, rz]

    elif line[0].lower() == "not":
        rx, rz = int(line[1][1:]), int(line[2][1:])
        b = [0b0111, rx, rz, 0b0000] 

    elif line[0].lower() == "shl":
        rx, v = int(line[1][1:]), int(line[2])
        b = [0b1000, rx, v, 0b0000]

    elif line[0].lower() == "shr":
        rx, v = int(line[1][1:]), int(line[2])
        b = [0b1001, rx, v, 0b0000]

    elif line[0].lower() == "inc":
        rx = int(line[1][1:])
        b = [0b1010, rx, 0b0000, 0b0000]

    elif line[0].lower() == "dec":
        rx = int(line[1][1:])
        b = [0b1011, rx, 0b0000, 0b0000]

    elif line[0].lower() == "mvi":
        rx, v = int(line[1][1:]), int(line[1][1:])
        b = [0b1100, rx, v, 0b0000]

    elif line[0].lower() == "load":
        rx, a = int(line[1][1:]), int(line[2])
        b = [0b1101, rx, a, 0b0000]

    elif line[0].lower() == "store":
        rx, a = int(line[1][1:]), int(line[2])
        b = [0b1110, rx, a, 0b0000]

    elif line[0].lower() == "jump":
        rx, a = int(line[1][1:]), int(line[2])
        b = [0b1111, rx, a, 0b0000]
    
    print(b)