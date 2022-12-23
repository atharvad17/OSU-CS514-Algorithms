from heapdict import heapdict
import heapq

def shortest(n, a):
    arr=[[] for i in range(0, n)]
    for i in range(0, len(a)):
        arr[a[i][0]].append((a[i][1], a[i][2]))
        arr[a[i][1]].append((a[i][0], a[i][2]))

    back = [1000 for i in range(0, n)]
    s=[]
    w = [1000 for i in range(0, n)]
    w[0] = 0
    d = heapdict()
    d[0] = 0
    res = [0]
    x = n-1

    while len(d) > 0:
        v = d.popitem()
        for i in range(0, len(arr[v[0]])):
            if (w[v[0]]+arr[v[0]][i][1]) < w[arr[v[0]][i][0]]:
                w[arr[v[0]][i][0]] = (w[v[0]]+arr[v[0]][i][1])
                d[arr[v[0]][i][0]] = w[arr[v[0]][i][0]]
                back[arr[v[0]][i][0]] = v[0]
    while x != 0:
        if(back[x] == 1000):
            return
        res.insert(1, x)
        x = back[x]
    return (w[n-1], res)