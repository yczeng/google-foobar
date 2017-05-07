def answer(l):
    #initialize dictionary of each number and its divisors with mod 0
    divs = [0] * len(l)
    counts = []

    for i in range(len(l)-1, -1, -1):
        num = l[i]
        divs[i] = []
        count = 0
        for j, div in enumerate(l[:i]):
            if num % div == 0:
                divs[i].append(j)
                count += 1
        counts = [count] + counts

    return sum([counts[i] for j in divs for i in j])

    # one = ""
    # two = ""
    # three = ""

    # count = 0
    # for i in range(len(l)-1, -1, -1):
    #     three = l[i]

    #     if divs[i] != []:
    #         for j in range(len(divs[i]) - 1, -1, -1):
    #             two = l[j]

    #             if divs[j] != []:
    #                 for k in range(len(divs[j]) - 1, -1, -1):
    #                     one = l[k]
    #                     #print((one, two ,three))
    #                     count += 1
    # return count
    
    
# store a dictionary
# key:indexes
# values: other indexes that are its divisors with mod 0

#testcases
print(answer([1,1,1]))
print(answer([1,2,3,4,5,6]))