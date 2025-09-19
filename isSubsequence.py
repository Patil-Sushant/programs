def isSubsequence(s, t):
    if len(t) == 0:
        return False
    elif len(s) > len(t):
        return False
    else:
        j = 0
        i = 0
        while i < len(t) and j < len(s):
            if s[j] == t[i]:
                j+=1
            i+=1
            if j == len(s):
                return True
    return False

print(isSubsequence('da', 'abcde'))