
lowerCaps = 'abcdefghijklmnopqrstuvwxyz'
upperCaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
specialChars = '!@#$%^&*()_+-={}[]|:";<>,.?/\\'


def checkPasswordStrength(s):
    if len(s) < 8:
        return 'Password should have at least 8 characters'
    elif len(s) >= 8 and len(s) <= 14:
        result = countUppercaseDigitSpecialChars(s)
        return result
       
    elif len(s) > 14 and len(s) <= 20:
        totalCount = countUppercaseDigitSpecialChars(s)
        validity = determineValidity(totalCount)
        return validity

def countUppercaseDigitSpecialChars(s):
    specialChar = False
    digit = False
    upperCap = False
    lowerCap = False

    for x in s:
        if x in lowerCaps:
            lowerCap = True
        if x in upperCaps:
            upperCap = True
        elif x in digits:
            digit = True
        elif x in specialChars:
            specialChar = True
    if upperCap == False or digit == False or specialChar == False or lowerCap == False:
        return 'Invalid password!'
    else:
        return 'Valid password!'
    
print(checkPasswordStrength('123$%^WERxyz'))

        

# elif len(s) > 14 and len(s) <= 20:
#     for x in s:
#         if x in upperCaps or x in digits or x in specialChars:
#             count += 1
#         if count >= 3:
#             print('Valid password!')
#         else:
#             return False
#             quit()

# def determineValidity(num):
#     if num >= 3:
#         return 'Valid password!'
#     else:
#         return 'Invalid password!'