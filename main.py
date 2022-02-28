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
# updateLoop = []
saveLoopAddress = []
saveLoopIndex = []

accepted = ['>', '<', '.', ',', '[', ']', '+', '-', '~', '?', '*', '/', '&']

'''
new ops:
~: copys a number from one part of the tape to another, e.g: >++<~> this code moves to the first index increments twice woves back to the 0 index then copys the 0 index to the 1st index
?: compares two numbers on the tape, ? is equal to, ?? is greater than, ??? is less than, and stores the result (1 or 0) in the index next to the second number
*: multiplies two numbers on the tape, bring the pointer to the number you want to multiply, this number will be multiplied by the number next to it and stored in the number next to that
/: divides two number on the tape, works the same as the * op just with / instead. NOTE if the / op returns a decimal nothing will be changed
&: jumps to a part of the tape and uses the current value the pointer is pointing at as an addres, NOTE because of the fact numbers can only be 0 or FF (255) you can only jump through 0-255
#: jumps to an address like & but only if the pointer+1 val is 1
'''

copyVal = 0
compareVal = 0
amComparing = 0

i = 0
while i != len(card):
    if card[i] in accepted:
        # news ones
        if card[i] == '#':
            if tape[pointer+1] == 1:
                pointer = tape[pointer]
        if card[i] == '&':
            pointer = tape[pointer]
        if card[i] == '*':
            tape[pointer+2] = tape[pointer]*tape[pointer+1]
        if card[i] == '/':
            maintain = tape[pointer+2]
            tape[pointer+2] = tape[pointer]/tape[pointer+1]
            if isinstance(tape[pointer+2], float)
                tape[pointer+2] = maintain
        if card[i] == '~':
            copyVal = tape[pointer]
            # while loop
            while True:
                if card[i] != ' ' and card[i] != '\n' and card[i] != '\t' and card[i] != '<' and card[i] != '>':
                    tape[pointer] = copyVal
                    break
                elif card[i] == '>':
                    pointer += 1
                elif card[i] == '<':
                    pointer -= 1
                i += 1
        if card[i] == '?':
            compareVal = tape[pointer]
            if card[i+1] == '?':
                if card[i+2] == '?':
                    amComparing = 2
                    i += 3
                else:
                    amComparing = 1
                    i += 2
            else:
                amComparing = 3
            # while loop
            while True:
                if card[i] != ' ' and card[i] != '\n' and card[i] != '\t' and card[i] != '<' and card[i] != '>':
                    if amComparing == 3:
                        if compareVal == tape[pointer]:
                            tape[pointer+1] = 1
                        else:
                            tape[pointer+1] = 0
                    if amComparing == 1:
                        if comparteVal > tape[pointer]:
                            tape[pointer+1] = 1
                        else:
                            tape[pointer+1] = 0
                    if amComparing = 2:
                        if compareVal < tape[pointer]:
                            tape[pointer+1] = 1
                        else:
                            tape[pointer+1] = 0
                    break
                elif card[i] == '>':
                    pointer += 1
                elif card[i] == '<':
                    pointer -= 1
                i += 1
        # defaults
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
        if card[i] == '[':
            saveLoopAddress.append(tape[pointer])
            saveLoopIndex.append(i+1)
        if card[i] == ']':
            if saveLoopAddress[saveLoopAddress] == 0:
                saveLoopAddress.pop(len(saveLoopAddress)-1)
                saveLoopIndex.pop(len(saveLoopIndex)-1)
            else:
                i = saveLoopIndex(len(saveLoopIndex)-1)
    if 
    i += 1
print(f'pointer: {pointer}\ntape: {tape}')