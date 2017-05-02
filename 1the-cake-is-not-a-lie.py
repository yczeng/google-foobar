def answer(s):
    if not s: #returns 0 if given invalid input
        return 0
        
    length = len(s)
    for i in range(len(s), 0, -1): #iterates from length of M&Ms to 1, i representing numM&Ms
        if length % i == 0:
            n = length/i
            c_slice = s[:n] #cake slice measured by unit of M&Ms
            
            boo = True
            for j in range(0, i):
                if s[j*n: j*n+n] != c_slice:
                    boo = False
        if boo:
            return i
    return 0