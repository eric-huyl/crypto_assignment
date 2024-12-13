import math
import sys

P = 1009
Q = 3063
N = P * Q
A = (P - 1) * (Q - 1)


def find_coprimes():
    coprimes = []
    for e in range(1, A):
        if math.gcd(e, A) == 1:
            print(f'Find e:{e}')
            coprimes.append(e)
    return coprimes


def check_non_encrypted(e) -> int:
    sum = 0
    for m in range(0, N - 1):
        if pow(m, e, N) == m:
            print(f'Find non-encrypted: m:{m} e:{e}')
            sum += 1
    return sum


def main():
    e_list = find_coprimes()
    with open('p3_1.out', 'w') as f:
        for e in e_list:
            sum = check_non_encrypted(e)
            f.write(f'e: {e},sum: {sum}')

main()
