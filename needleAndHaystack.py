def needleAndHaystack(needle, haystack):
    if len(needle) == 0:
        return 'no needle'
    elif len(haystack) == 0:
        return 'no haystack'
    i = 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i: i+len(needle)] == needle:
            return i
    return False
   
print(needleAndHaystack('but', 'sadbutsad'))