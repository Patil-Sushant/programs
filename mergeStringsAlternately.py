def mergeStringsAlternately(s, t):
    i, j = 0, 0
    result = []
    while i < len(s) and j < len(t):
        result.append(s[i])
        result.append(t[j])
        i += 1
        j += 1
    result.append(s[i:])
    result.append(t[j:])
    
    return ''.join(result)

print(mergeStringsAlternately('abc', 'pqrst'))

"""
lines 9, 10 - what you are doing here is appending the rest of the chars from s or t to the array after 
the index goes out of bounds on one of them. The reason why we have an array is because strings are immuatable in python
imagine, result = '' and you did result = result + .. That would create a new string everytime something was appended to it .
so in line 12, an empty string is used as the delimiter to join all the chars together using join()
"""

# https://leetcode.com/problems/merge-strings-alternately/description/
# https://www.youtube.com/watch?v=LECWOvTo-Sc&pp=ygUgbWVyZ2Ugc3RyaW5ncyBhbHRlcm5hdGVseSBweXRob24%3D