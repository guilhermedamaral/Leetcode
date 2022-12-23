
def romanToInt(values):
    for s in values:
        letters = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        value, ancestor = 0, 1001
        for let in s:
            if letters[let] > ancestor and ancestor > 0:
                value += letters[let]
                value -= ancestor*2
            
            else:
                value += letters[let]
                ancestor = letters[let]

        print(f"{s}: {value}")
    return

values = ["III", "LVIII", "MCMXCIV"]
romanToInt(values)
