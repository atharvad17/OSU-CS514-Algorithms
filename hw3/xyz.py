
def find(arr):
    tempResult = []
    result = []
    arr.sort()
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) <= arr[len(arr)-1]:
                temp = (arr[i], arr[j], arr[i] + arr[j])
                tempResult.append(temp)
            else:
                break
    for i in range(2, len(arr)):
        for j in range(0, len(tempResult)):
            if arr[i] == tempResult[j][2]:
                result.append(tempResult[j])
    return result