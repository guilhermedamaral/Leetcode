
def romanToInt(s):
    letters = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
    value, ancestor = 0, 1001
    for let in s:
        if letters[let] > ancestor and ancestor > 0:
            value += letters[let]
            value -= ancestor*2
        
        else:
            value += letters[let]
            ancestor = letters[let]

    print(value)
    return value

s = "III"
romanToInt(s)
s = "LVIII"
romanToInt(s)
s = "MCMXCIV"
romanToInt(s)