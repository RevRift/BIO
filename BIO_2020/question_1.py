print('Name')
print('School/college')

# question 1a
from itertools import groupby

arr = (('I', 1), ('IV', 4), ('V', 5), ('IX', 9), ('X', 10), ('XL', 40), ('L', 50), ('XC', 90), ('C', 100), ('CD', 400), ('D', 500), ('DM', 900), ('M', 1000))

def dec_to_roman(dec):
    try:
        roman = ''
        for i in range(len(arr) - 1, -1, -1):
            while arr[i][1] <= dec:
                dec -= arr[i][1]
                roman += arr[i][0]
        return roman
    except:
        return False

def look_and_say(s):
    ret = ''
    for char, group in groupby(s):
        ret += dec_to_roman(len(''.join(group))) + char
    return ret

roman_numeral, n = input().split()

for _ in range(int(n)):
    roman_numeral = look_and_say(roman_numeral)

print(roman_numeral.count('I'), roman_numeral.count('V'))

# question 1b
valid = set(dec_to_roman(i) for i in range(1, 4000)) # description is a maximum of 2000 as there are at most 2 Ms in a roman numeral from 1 to 3999
for dec in range(1, 4000):
    roman = dec_to_roman(dec)
    description = look_and_say(roman)
    if description in valid:
        print(description)

# question 1c
print(len(set(look_and_say(dec_to_roman(i)) for i in range(1, 4000))))