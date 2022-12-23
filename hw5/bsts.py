dict = {0: 1}

def bsts(n):
    temp = 0
    if n not in dict:
        for i in range(1, n+1):
            temp += (bsts(i-1) * bsts(n-i))
            dict[n] = temp
    return dict[n]


print(bsts(5))