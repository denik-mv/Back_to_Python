foo = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
       'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
       'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

numr = 'MCMXCVII'
res = 0
skip = 0

for i in range(len(numr)):
    if i+1 == len(numr):
        res += foo[numr[i]]
        break
    if foo[numr[i]] >= foo[numr[i+1]] and skip == 0:
        res += foo[numr[i]]
    elif skip == 1:
        skip = 0
        continue
    else:
        res += foo[numr[i] + numr[i+1]]
        skip = 1

print(res)
