def mergesort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    leftArr = mergesort(arr[:mid])
    rightArr = mergesort(arr[mid:])
    return merge(leftArr, rightArr)


def merge(leftArr, rightArr):
    resultArr = []
    i = j = 0
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            resultArr.append(leftArr[i])
            i += 1
        else:
            resultArr.append(rightArr[j])
            j += 1

    resultArr.extend(leftArr[i:])
    resultArr.extend(rightArr[j:])

    return resultArr