from heapq import heappush, heappop
from collections import defaultdict

rnaPair = set(['AU', 'GC', 'GU', 'UA', 'CG', 'UG'])

def best(rna):
    def _best(i, j):
        if (i, j) in opt:
            return opt[i, j]
        curr = -1
        for k in range(i, j):
            if _best(i, k) + _best(k + 1, j) > curr:
                curr = max(curr, _best(i, k) + _best(k + 1, j))
                back[i, j] = k
        if rna[i] + rna[j] in rnaPair:
            if _best(i + 1, j - 1) + 1 > curr:
                curr = _best(i + 1, j - 1) + 1
                back[i, j] = -1
        opt[i, j] = curr
        return curr

    def solution(i, j):
        if (i == j):
            return "."
        if (i > j):
            return ""
        k = back[i, j]
        if (k == -1):
            return "(%s)" % solution(i + 1, j - 1)
        else:
            return solution(i, k) + solution(k + 1, j)

    opt = defaultdict(int)
    back = {}
    n = len(rna)
    for i in range(n):
        opt[i, i] = 0
        opt[i, i - 1] = 0
    return _best(0, n - 1), solution(0, n - 1)


def total(rna):
    def _total(i, j):
        if (i, j) in opt:
            return opt[i, j]
        count = 0
        for k in range(i, j):
            if rna[j] + rna[k] in rnaPair:
                count += _total(i, k - 1) * _total(k + 1, j - 1)
        count += _total(i, j - 1)
        opt[i, j] = count
        return count

    opt = defaultdict(int)
    n = len(rna)
    for i in range(n):
        opt[i, i] = 1
        opt[i, i - 1] = 1
    return _total(0, n - 1)
    return 0


def kbest(rna, k):
    def _kbest(i, j):

        def binaryPush(s, p, q):
            if p < len(kList[i, s]) and q < len(kList[s + 1, j]) and (s, p, q) not in visited:
                heappush(h, (- (kList[i, s][p][0] + kList[s + 1, j][q][0]), (s, p, q)))
                visited.add((s, p, q))

        def unaryPush(p):
            if p < len(kList[i + 1, j - 1]):
                heappush(h, (- (kList[i + 1, j - 1][p][0] + 1), (p,)))

        if (i, j) in kList:
            return kList[i, j]
        if (i == j):
            kList[i, j] = [(0, '.')]
            return
        elif (j == i - 1):
            kList[i, i - 1] = [(0, '')]
            return

        h = []
        visited = set()
        for s in range(i, j):
            _kbest(i, s)
            _kbest(s + 1, j)
            binaryPush(s, 0, 0)
        if rna[i] + rna[j] in rnaPair:
            _kbest(i + 1, j - 1)
            unaryPush(0)
        found = 0
        while found < k:
            if (h == []):
                break
            score, indices = heappop(h)
            try:
                s, p, q = indices
                ans = (-score, "%s%s" % (kList[i, s][p][1], kList[s + 1, j][q][1]))
                if ans not in kList[i, j]:
                    kList[i, j].append(ans)
                    found += 1
                binaryPush(s, p + 1, q)
                binaryPush(s, p, q + 1)
            except:
                p = indices[0]
                ans = (-score, "(%s)" % kList[i + 1, j - 1][p][1])

                if ans not in kList[i, j]:
                    kList[i, j].append(ans)
                    found += 1

                unaryPush(p + 1)

    kList = defaultdict(list)
    past = {}
    n = len(rna)
    _kbest(0, n - 1)
    return _kbest(0, n - 1)
    return 0