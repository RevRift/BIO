"""
ideas:
choose two letters to be connected and ensure none of the others connect
generate first plan and try and get to the next plan from the previous one
generation a function using integers (maybe from 0 to p-1) and try and mathematically see if the alphabetical ordering is also the numerical ordering

how about you start with an int array [0, 0, 0, 0] and you have an increment() function that moves the array up to the next valid array of letter_codes_
maybe working with integers will let the code run fast
"""

# arr = ['AABA', 'AABB', 'ABAA', 'ABAB', 'ABBA', 'BAAB', 'BABB', 'BBAA', 'BBAB']
# to_codes = lambda s: ''.join(str(ord(char) - ord('A')) for char in s)
# for string in arr:
# print(string, to_codes(string), int(to_codes(string), 2))

p, q, r = map(int, input().split())
