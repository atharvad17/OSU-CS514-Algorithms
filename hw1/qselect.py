
import random

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
