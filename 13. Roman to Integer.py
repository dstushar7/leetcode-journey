# https://leetcode.com/problems/roman-to-integer/



s = 'MCMXCIV'

values = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,}

sum = 0
subtraction = 0


for i in range(len(s)):
    # If subtraction signal found, skip the next character
    if subtraction == 1:
        subtraction = 0
        continue
    
    if i == (len(s)-1):
        sum = sum + values[s[i]]
        break


    # Checking of 6 instances and adding the value
    if s[i] == 'I':
        if s[i+1] == 'V':
            subtraction = 1
            sum = sum + 4
            continue
        if s[i+1] == 'X':
            subtraction = 1
            sum = sum + 9
            continue


    if s[i] == 'X':
        if s[i+1] == 'L':
            subtraction = 1
            sum = sum + 40
            continue
        if s[i+1] == 'C':
            subtraction = 1
            sum = sum + 90
            continue

    if s[i] == 'C':
        if s[i+1] == 'D':
            subtraction = 1
            sum = sum + 400
            continue
        if s[i+1] == 'M':
            subtraction = 1
            sum = sum + 900
            continue

    #If it doesn't fall in any condition then just add the main value 
    sum = sum + values[s[i]]

print(sum)

