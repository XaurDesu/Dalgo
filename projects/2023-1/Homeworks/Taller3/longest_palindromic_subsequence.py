from itertools import combinations

def get_subsequences(s):
    out = set()
    for i in range(1, len(s) + 1):
        for c in combinations(s, i):
            if c[::-1] == c:
                out.add(''.join(c))
    return sorted(out, reverse=True, key=len)

def longest_palindromic_subsequence(s: str) -> int:
    strings = get_subsequences(s)
    return len(strings[0])