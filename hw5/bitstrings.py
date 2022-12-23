dict = {0: 1, 1: 2}

def num_no(n):
    if n not in dict:
        dict[n] = num_no(n - 1) + num_no(n - 2)
    return dict[n]

def num_yes(n):
    temp = num_no(n)
    return pow(2, n) - temp