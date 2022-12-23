
import sys
import bisect

def find(arr, x, k):
    q = (bisect.bisect(arr, x))
    p = q-1
    result = []
    while k != 0:
        if q == len(arr) or abs(x-(arr[p])) <= abs(x-(arr[q])):
            p = p-1
        else:
            q = q+1
        k = k-1
    for i in range(p+1, q):
        result.append(arr[i])
    return result