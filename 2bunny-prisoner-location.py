def answer(x, y):
    i = 1
    ans = 0
    while i <= x:
        ans += i
        print(i)
        i += 1

    i -= 1
    j = 1
    while j < y:
    	ans += i
    	j += 1
    	i += 1

    return str(int(ans))