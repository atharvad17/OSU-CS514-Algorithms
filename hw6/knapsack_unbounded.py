
def best(w, arr):
    dp = [0 for i in range(w + 1)]
    c = [[] for _ in range(w + 1)]
    res = [0 for i in range(len(arr))]
    for i in range(w + 1):
        for j in range(len(arr)):
            if (arr[j][0] <= i):
                if (dp[i] < dp[i - arr[j][0]] + arr[j][1]):
                    dp[i] = dp[i - arr[j][0]] + arr[j][1]
                    c[i] = [j] + c[i - arr[j][0]]

    for i in range(len(c[w])):
        res[c[w][i]] += 1
    return dp[w], res