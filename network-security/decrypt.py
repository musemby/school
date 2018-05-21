"""
    A simple Caesar cipher implementation for decrypting a message
    By: Joseph Musembi
        P15/1559/2015
"""

def get_user_input():
    print('Type in the cipher to be decrypted')
    return raw_input()


def get_decryption_key():
    print("Enter decryption key: ")
    key = int(raw_input())
    if key >= 1 and key <= 26:
        # decryption key is negative of encryption key
        return -key


def decrypt(cipher, key):
    decrypted = ""

    for symbol in cipher:
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

            decrypted += chr(ordinal)
        else:
            # non alphabetic
            decrypted += symbol

    return decrypted


if __name__ == '__main__':
    cipher = get_user_input()
    key = get_decryption_key()

    decrypted = decrypt(cipher, key)

    print("Cipher: \n {} \n has been decrypted to: \n {}".format(cipher, decrypted))