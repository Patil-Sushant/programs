
def stringCompress(s):
    count = 1
    result = ''
    if len(s) == 0:
        return 'empty string'
    elif len(s) == 1:
        result = s + str(count)
        return result
    else:
        # print('hello')
        for p in range(1, len(s)):
            if s[p] == s[p-1]:
                count += 1
            else:
                result = result + s[p-1] + str(count)
                count = 1
        result = result + s[-1] + str(count)
        return result

print(stringCompress('abbbccaa'))


# st = 'javascript'
# print(st[-1])


"""

https://www.askpython.com/python/list/negative-indexing

Negative Indexing in List

Sometimes, we are interested in the last few elements of a list or maybe we just want to index the list from the opposite end, we can use negative integers.

The process of indexing from the opposite end is called Negative Indexing. In negative Indexing, the last element is represented by -1.

Example:

1
2
3
4
5
my_list = [45, 5, 33, 1, -9, 8, 76]
 
print(my_list[-1]) 
print(my_list[-2])
print(my_list[-3])
Output:
76
8
-9
"""

# References
# https://blog.finxter.com/5-best-ways-to-perform-string-compression-in-python/