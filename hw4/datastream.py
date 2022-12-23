import heapq

def ksmallest(k, arr):
	n = len(arr)
	pq = []
	result = []
	for i in range(n):
		heapq.heappush(pq, -1*arr[i])
		if len(pq) > k:
			heapq.heappop(pq)

	while len(pq) != 0:
		result.append(heapq.heappop(pq)*-1)
	result.reverse()
	return result