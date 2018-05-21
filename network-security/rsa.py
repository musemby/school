"""
    Implementation of the Rivest-Shamir-Adleman (RSA) public key encryption algorithm
    Author: @musemby
"""
import math
import random
import sys

MAX = 1000


def _is_prime(x):
    n = 0
    if x < 2:
        return False

    for i in range(2, x//2+1):
        if x % i == 0:
            n = n + 1

    return n <= 0


def _get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def _generate_primes():
    """
        Generates prime numbers from 2 to MAX
    """
    for i in range (2, MAX):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        else:
            yield i


def _get_single_prime():
    integer = random.randint(2, MAX)

    if not _is_prime(integer):
        _get_single_prime()
    return integer


def _pick_random_primes():
    return _get_single_prime(), _get_single_prime()


def _get_prime_product(p, q):
    return p * q


def _compute_totient(p, q):
    return (p-1) * (q-1)


# def _compute_encryption_key(Tn):
#     primes = []
#     for i in _generate_primes():
#         if i > 2 and Tn % i != 0:
#             primes.append(i)

#     return random.choice(primes)
    # return primes[1]
def _compute_encryption_key(Tn):
    e = random.randrange(1, Tn)
    gcd = _get_gcd(e, Tn)
    while gcd != 1:
        e = random.randrange(1, Tn)
        gcd = _get_gcd(e, Tn)

    return e


def _compute_decryption_key(e, phi):
    # for i in range(0, MAX):
    #     d = (1 + (i * Tn))/e
    #     if d > 0 and isinstance(d, int):
    #         return d

    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi


def encrypt(number, e, n):
    return number**e % n


def decrypt(cipher, d, n):
    return cipher**d % n


if __name__ == '__main__':
    p = int(input("Enter the first prime number"))
    q = int(input("Enter the second prime number"))

    n = _get_prime_product(p, q)
    Tn = _compute_totient(p, q)
    e = _compute_encryption_key(Tn)
    _d = _compute_decryption_key(e, Tn)
    # import pdb; pdb.set_trace()
    cipher = encrypt(23242, e, n)
    data = decrypt(cipher, _d, n)
    print("n: {}, Tn: {}, e: {}, d: {}".format(n, Tn, e, _d))
    print("Encrypted {} to: {}".format(data, cipher))
    print("Decrypted {} to: {}".format(cipher, data))
