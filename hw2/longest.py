class LongLength:
    def __init(n):
        n.left = 0


def longest(tree):
    length = LongLength()
    return _longest(tree, length)

def _longest(tree, length):
    leftLength = LongLength()
    rightLength = LongLength()
    if tree == []:
        length.left = 0
        return 0

    L = _longest(tree[0], leftLength)
    R = _longest(tree[2], rightLength)
    length.left = max(leftLength.left, rightLength.left) + 1

    return max(leftLength.left + rightLength.left, max(L, R))