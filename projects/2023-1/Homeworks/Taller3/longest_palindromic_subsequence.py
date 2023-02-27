def is_palindromic(s):
    return s == s[::-1]
def longest_palindromic_subsequence(s):
    ret = ""
    strings = []

    for i in range(0,len(s)):
        for j in range(i, len(s)+1):
            sub = s[i:j]
            if sub in strings:
                pass
            strings.append(sub)
            if len(sub) > len(ret) and is_palindromic(sub):
                ret = sub
            
    return ret