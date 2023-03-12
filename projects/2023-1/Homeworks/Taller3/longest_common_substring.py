def longest_common_substring(str_1: str, str_2: str) -> str:
    ret = ""
    for i in range(0,len(str_1)):
        for j in range(i, len(str_1)+1):
            sub = str_1[i:j]
            if sub not in str_2:
                continue
            if len(sub) > len(ret):
                ret = sub
    return ret
