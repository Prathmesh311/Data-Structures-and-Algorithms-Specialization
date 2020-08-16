# python3
import random


def compute_hash(s, x, p):
    hash = 0
    for i in reversed(s):
        hash = (hash * x + ord(i)) % p
    return hash


def precomputed_hashes(text, pattern, p, x):
    H = [None] * (len(text) - len(pattern) + 1)
    # s = text[(len(text) - len(pattern)): len(text) - 1]
    s = text[-len(pattern):]
    H[len(text) - len(pattern)] = compute_hash(s, x, p)
    y = 1
    for i in range(1, len(pattern) + 1):
        y = (y * x) % p
    for i in reversed(range(len(text) - len(pattern))):
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + len(pattern)]))
        while(H[i] < 0):
            H[i] += p
        H[i] = H[i] % p
    return H


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    p = 10000007
    s = random.randint(1, p)
    PHash = compute_hash(pattern, s, p)
    H = precomputed_hashes(text, pattern, p, s)
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if H[i] == PHash and text[i:i + len(pattern)] == pattern
    ]


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
