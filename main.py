import os

while True:
    fileName = input('Enter the name of file > ')
    if fileName.endswith('.bfp'):
        break
    else:
        print('Enter a .bfp file')

f = open(fileName, 'r')
card = f.read()
f.close()

pointer = 0
tape = [0]
updateLoop = []
saveLoopAddress = []
saveLoopIndex = []

accepted = ['>', '<', '.', ',', '[', ']', '+', '-', '~', '?', '*', '/', '&']

'''
new ops:
~: copys a number from one part of the tape to another
?: compares two numbers on the tape, ? is equal to, ?? is greater than, ??? is less than
*: multiplies two numbers on the tape, bring the pointer to the number you want to multiply then use the op then use the '<' or '>' ops to bring the pointer to the second number. The output of this operation will be stored at the first number
/: divides two number on the tape, works the same as the * op just with / instead. NOTE if the / op returns a decimal nothing will be changed
&: jumps to a part of the tape and uses the current value the pointer is pointing at as an addres, NOTE because of the fact numbers can only be 0 or FF (255) you can only jump through 0-255
'''

i = 0
while i != len(card):
    if card[i] in accepted:
        if card[i] == '+':
            tape[pointer] += 1
            if tape[pointer] > 255:
                tape[pointer] == 0
        if card[i] == '-':
            tape[pointer] -= 1
            if tape < 0:
                tape[pointer] == 255
        if card[i] == '>':
            pointer += 1
            try:
                if tape[pointer] == 0:
                    print(' ', end='')
            except:
                tape.append(0)
        if card[i] == '<':
            pointer -= 1
            if pointer < 0:
                pointer = 0
        if card[i] == '.':
            print(chr(tape[pointer]))
        if card[i] == ',':
            io = input()
            tape[pointer] = ord(io[0])
            if tape[pointer] > 255:
                tape[pointer] = 0

        