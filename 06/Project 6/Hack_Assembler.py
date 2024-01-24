from argparse import ArgumentParser, Namespace

parser = ArgumentParser()
parser.add_argument('file_name', help= "name of the file")
args = parser.parse_args()

n = 16

comp_codes = {
            "0": "0101010",
            "1": "0111111",
            "-1": "0111010",
            "D": "0001100",
            "A": "0110000",
            "!D": "0001101",
            "!A": "0110001",
            "-D": "0001111",
            "-A": "0110011",
            "D+1": "0011111",
            "A+1": "0110111",
            "D-1": "0001110",
            "A-1": "0110010",
            "D+A": "0000010",
            "D-A": "0010011",
            "A-D": "0000111",
            "D&A": "0000000",
            "D|A": "0010101",
            "M": "1110000",
            "!M": "1110001",
            "-M": "1110011",
            "M+1": "1110111",
            "M-1": "1110010",
            "D+M": "1000010",
            "D-M": "1010011",
            "M-D": "1000111",
            "D&M": "1000000",
            "D|M": "1010101",
        }
jump_codes = {"null": '000',
              "JGT": "001",
              "JEQ": "010",
              "JGE": "011",
              "JLT": "100",
              "JNE": "101",
              "JLE": "110",
              "JMP": "111"}

dest_codes = {"null": '000',
              "M": '001',
              "D": '010',
              "MD": '011',
              "A": '100',
              "AM": '101',
              "AD": '110',
              "AMD": '111'}
defined_symbols = {
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,
            "SCREEN": 0x4000,
            "KBD": 0x6000,
        }

def getInput(file_name):
    with open(file_name, mode= "r") as file:

        inputs = [x.strip() for x in file.readlines()]

        inputs = filterComments(inputs)

        inputs = filterSpaces(inputs)
    return inputs


def filterSpaces(array):
    a =  list(filter(None, array))
    return a

def filterComments(array):
    a = [line for line in array if line[:1] != '/']

    b = [line[:line.find('/')].strip() if '/' in line else line for line in a]

    return b

def writeOutput(array):
    with open("result.hack", 'w') as file:
        for line in array:
            print(line, file= file)

def cInstruction(instruction):
    if ";" in instruction:
        jump_i = instruction[instruction.find(";") + 1 : ]

        if "=" in instruction:
            dest_i = instruction[ : instruction.find("=")]
            comp_i = instruction[instruction.find("=") + 1 : instruction.find(";")]
        else:
            comp_i = instruction[ : instruction.find(";")]
            dest_i = 'null'
    else:
        jump_i = 'null'

        if "=" in instruction:
            dest_i = instruction[ : instruction.find("=")]
            comp_i = instruction[instruction.find("=") + 1 : ]
        else:
            comp_i = '0'
            dest_i = 'null'


    jump_i, comp_i, dest_i = [s.strip() for s in (jump_i, comp_i, dest_i)]
    final = "111"
    print(jump_i, comp_i, dest_i)

    comp = comp_codes[comp_i]
    dest = dest_codes[dest_i]
    jump = jump_codes[jump_i]

    return final + comp + dest + jump

def aInstruction(instruction):
    global n

    if instruction.isnumeric():
        num = int(instruction)
    else:
        if instruction in defined_symbols:
            num = defined_symbols[instruction]
        else:
            defined_symbols[instruction] = n
            num = n
            n += 1
    # To handle the symbols

    return "0" + str(bin(num))[2:].zfill(15)

def firstPass(array):
    count = 0
    for i in range(len(array)):
        print(array[i])
        if array[i][0] == "(":
            defined_symbols[array[i][1: len(array[i])- 1]] = i - count
            count += 1

def main():
    list_r = []

    inputs = getInput(args.file_name)
    firstPass(inputs)

    for line in inputs:
        if line[:1] == '@':
            list_r.append(aInstruction(line[1:]))
        elif line[:1] == '(':
            continue
        else:
            list_r.append(cInstruction(line))

    writeOutput(list_r)

main()