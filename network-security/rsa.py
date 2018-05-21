"""
    Implementation of the Rivest-Shamir-Adleman (RSA) public key encryption algorithm
    Author: @musemby
"""
import math
import random
import sys

MAX = 1000

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
    stop = random.randint(MAX/2, MAX)
    for x in _generate_primes():
        if x > stop:
            return(x)


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
def get_encryption_key(Tn):
    e = random.randrange(1, Tn)
    gcd = _get_gcd(e, Tn):
    while gcd != 1:
        e = random.randrange(1, Tn)
        gcd = gcd(e, Tn)

    return e


def _compute_decryption_key(e, Tn):
    for i in range(0, MAX):
        d = (1 + (i * Tn))/e
        if d > 0 and isinstance(d, int):
            return d


def encrypt(number, e, n):
    return number**e % n


def decrypt(cipher, d, n):
    return cipher**d % n


class Node():

    def __init__(self, ):
        pass

    


if __name__ == '__main__':
    p, q = _pick_random_primes()
    # p, q = 11, 5
    n = _get_prime_product(p, q)
    Tn = _compute_totient(p, q)
    e = _compute_encryption_key(Tn)
    d = _compute_decryption_key(e, Tn)
    cipher = encrypt(2, e, n)
    data = decrypt(cipher, d, n)
    print("n: {}, Tn: {}, e: {}, d: {}".format(n, Tn, e, d))
    print("Encrypted 2 to: {}".format(cipher))
    print("Encrypted {} to: {}".format(cipher, data))
