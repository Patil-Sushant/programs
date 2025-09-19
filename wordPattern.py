# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         listOfStrings = s.split(' ')
#         list1 = []
#         list2 = []

#         for i in pattern:
#             list1.append(pattern.index(i))
#         print(list1)

#         for i in listOfStrings:
#             list2.append(listOfStrings.index(i))
#         print(list2)

#         if list1 == list2:
#             return True
#         else:
#             return False

# a = Solution()
# print(a.wordPattern('abba', 'dog cat cat bat'))

# above solution using Class is also correct



def wordPattern(pattern: str, s: str) -> bool:
    words = s.split(' ')
    if len(words) != len(pattern):
        return False

    listOfStrings = s.split(' ')
    list1 = []
    list2 = []

    for i in pattern:
        list1.append(pattern.index(i))
    print(list1)

    for i in listOfStrings:
        list2.append(listOfStrings.index(i))
    print(list2)

    if list1 == list2:
        return True
    else:
        return False

print(wordPattern('abba', 'dog cat cat dog'))

"""
# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150

# def isWordPattern(pattern, s):
    # words = s.split(' ')
    # if len(words) != len(pattern):
    #     return False
#     pToStr = {} # pattern to string
#     strToP = {} #string to Pattern

# https://leetcode.com/problems/word-pattern/solutions/4686871/very-easy-python3-solution/?envType=study-plan-v2&envId=top-interview-150
# checkout this link as well: https://auditorical.com/word-pattern-leetcode/
"""