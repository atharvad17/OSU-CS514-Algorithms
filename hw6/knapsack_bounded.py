
def best(w, arr):
    dp = [0 for i in range(w + 1)]
    c = [[0 for i in range(len(arr))] for j in range(w + 1)]
    for i in range(w + 1):
        for j in range(len(arr)):
            if (arr[j][0] <= i):
                if (dp[i] < dp[i - arr[j][0]] + arr[j][1] and (c[i - arr[j][0]][j] < arr[j][2])):
                    c[i] = c[i - arr[j][0]].copy()
                    c[i][j] += 1
                    dp[i] = dp[i - arr[j][0]] + arr[j][1]
    res = 0
    for i in range(w + 1):
        if dp[i] >= dp[res]:
            res = i

    return dp[res], c[res]