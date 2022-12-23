
import random

def find(arr1, x, k):
    arr2 = []
    result = []
    for i in range(0, len(arr1)):
        arr2.append(abs(arr1[i] - x))

    q = qselect(k, arr2)
    count = 0
    for i in range(0, len(arr1)):
        if abs(arr1[i] - x) <= q:
            count += 1
            result.append(arr1[i])
        if count == k:
            break
    return result

def qselect(k, arr):
    if (len(arr) < 0 or k == 0 or k > len(arr)):
        return []
    else:
        i = random.randint(0, len(arr) - 1)
        arr[0], arr[i] = arr[i], arr[0]
        pivot = arr[0]
        leftArr = [x for x in arr if x < pivot]
        pivotValue = len(leftArr)
        if k == pivotValue + 1:
            return pivot
        elif k < pivotValue + 1:
            return qselect(k, leftArr)
        else:
            rightArr = [x for x in arr[1:] if x >= pivot]
            return qselect(k - (pivotValue + 1), rightArr)