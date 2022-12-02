# Runtime 45 ms | Beats 80.65% | Memory 13.8 MB | Beats 77.84%

def halvesAreAlike(s):
    if len(s)%2 == 0:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l = int(len(s)/2)
        a = (s[0:l])
        b = s[l:]
        count_a = 0
        count_b = 0
        
        for i in a:
            if i in vowels:
                count_a += 1
        
        for i in b:
            if i in vowels:
                count_b += 1
            
        if count_a == count_b:
            print(True)
            return(True)
    
    print(False)
    return False
        
s =  "book"
halvesAreAlike(s)
s =  "textbook"
halvesAreAlike(s)
