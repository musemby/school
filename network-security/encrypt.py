"""
    A simple Caesar cipher implementation for encrypting a message
    By: Joseph Musembi
        P15/1559/2015
"""

def get_user_input():
    print('Type in the message to be encrypted:\n')
    return raw_input()


def get_encryption_key():
    print("Enter encryption key: ")
    key = int(raw_input())
    if key >= 1 and key <= 26:
        return key


def encrypt(message, key):
    encrypted = ""

    for symbol in message:
        if symbol.isalpha():
            ordinal = ord(symbol)
            ordinal += key

            if symbol.isupper():
                if ordinal > ord('Z'):
                    ordinal -= 26
                elif ordinal < ord('A'):
                    ordinal += 26

            elif symbol.islower():
                if ordinal > ord('z'):
                    ordinal -= 26
                elif ordinal < ord('a'):
                    ordinal += 26

            encrypted += chr(ordinal)
        else:
            # non alphabetic treat normally
            encrypted += symbol

    return encrypted


if __name__ == '__main__':
    message = get_user_input()
    key = get_encryption_key()

    encrypted = encrypt(message, key)

    print("Text: \n {} \n has been encrypted to: \n {}".format(message, encrypted))