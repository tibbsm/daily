

def decode(message):

    if len(message) <= 1:
        return 1

    if len(message) > 1:
        if 1 <= int(''.join(message[0:2])) <= 26:
            return (decode(message[1:]) + decode(message[2:]))

        return decode(message[1:])

print decode('111')
