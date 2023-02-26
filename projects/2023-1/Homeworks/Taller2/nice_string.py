from collections import Counter

def check_string(string:str):
    if len(string) < 2:
        return False
    count = Counter(string).keys()
    for i in count:
        if i.upper() in count and i.lower() in count:
            continue
        else:
            return False
    return True
    
def nice_string(string:str)->str:
    nicest = ""
    i = 0
    while i < len(string):
        j = i+1
        ret =""
        ret += string[i]
        while j < len(string):
            ret += string[j]
            if check_string(ret) and len(ret)>len(nicest):
                nicest = ret
            j += 1
        i += 1
    return nicest