def iteration():
    cmd = code[c_pointer]
    c_pointer += 1
    if cmd == '>':
        d_pointer +=1
    elif cmd == '<':
        d_pointer -=1
    elif cmd == '+':
        value = data.get(d_pointer, 0)
        value = 0 if value == 255 else value + 1
        data[d_pointer] = value
    elif cmd == '-':
        value = data.get(d_pointer, 0)
        value = 255 if value == 0 else value - 1
        data[d_pointer] = value
    elif cmd == '.':
        value = data.get(d_pointer, 0)
        output.append(value)
    elif cmd == ',':
        value = data.get(d_pointer, 0)
        d_pointer = value
    elif cmd == '[':
        value = data.get(d_pointer, 0)
        if value == 0:
            c_pointer = code.find(']', c_pointer) + 1
    elif cmd == ']':
        value = data.get(d_pointer, 0)
        if value != 0:
            c_pointer = code.rfind('[', 0, c_pointer) + 1
    else:
        assert(False, cmd)
     
def brain_luck(code, input):
    data = {i: ord(d) for i, d in enumerate(input)}
    output = []
    c_pointer = 0
    d_pointer = 0
    while(True):
        try:
            data, output, c_pointer, d_pointer = iteration(data, output, c_pointer, d_pointer)
        except IndexError:
            break
    return ''.join(chr(o) for x in output)

assert(
 (',+[-.,+]', 'Codewars' + chr(255)) == 'Codewars'
)

assert(
 brain_luck(',+[-.,+]', 'Codewars' + chr(255)) == 'Codewars'
)

## Echo until byte(0) encountered
#assert(
#        brain_luck(',[.[-],]', 'Codewars' + chr(0)) ==
#        'Codewars'
#        )
#
## Two numbers multiplier
#assert(
#    brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)) ==
#    chr(72)
#        )
