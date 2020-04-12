# ENCryt

def encrypt(text , shift=3):
    upper_c_t = text.upper()
    encrypted_t = []

    for c in upper_c_t:
        if c == ' ':
            encrypted_t.append(' ')
            continue
        x = (((ord(c)-65) + shift)% 26 ) + 65
        encrypted_t.append(chr(x))
    
    return "".join(encrypted_t)


# _______________________________
# DECRypt

def brute_force(msg):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for key in range(len(LETTERS)):
        translated = []
        for symbol in msg:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num-key
                if num<0:
                    num = num + len(LETTERS)
                translated.append(LETTERS[num])
            else:
                translated.append(symbol)

        print(f'Key={key}, message = {"".join(translated)}')

