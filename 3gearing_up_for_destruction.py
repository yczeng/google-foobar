def answer(pegs):
	dic = {}
	for i in range(len(pegs) - 1):
		dic[i] = pegs[i+1] - pegs[i]

	last_n = dic[len(pegs) - 2]

	boo = False
	for i in range(len(pegs) - 3, -1, -1):
		if boo == False:
			last_n -= dic[i]
		else:
			last_n += dic[i]
		boo = not boo

	if len(pegs) % 2 == 0:
		last_d = 3

		if last_n % 3 == 0:
			last_n /=3
			last_d = 1
	else:
		last_d = 1
		last_n = -last_n

	last_n *= 2

	radi = [last_n/last_d]
	for i, peg in enumerate(pegs[1:]):
		r = peg - pegs[i] - radi[-1]
		if r <= 0:
			return [-1, -1]
		else:
			radi.append(r)

	return [last_n, last_d]

# print(answer([4, 30, 50])) # should return [12, 1]
# print(answer([4, 17, 50]))