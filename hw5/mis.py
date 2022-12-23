
def max_wis(wpg):
    if wpg == []:
        return (0, [])
    for i in range(0, len(wpg)):
        if wpg[i] < 0:
            wpg[i] = 0
    n = len(wpg)
    solution_weights = [0] * (n + 1)
    solution_weights[0] = 0
    solution_weights[1] = wpg[0]

    for i in range(2, n + 1):
        solution_weights[i] = max(solution_weights[i - 1], solution_weights[i - 2] + wpg[i - 1])
    wis = []
    i = n
    while i >= 1:
        if solution_weights[i - 1] >= solution_weights[i - 2] + wpg[i - 1]:
            i = i - 1
        else:
            if wpg[i - 1] != 0:
                wis.insert(0, wpg[i - 1])
            i = i - 2
    return solution_weights[n], wis