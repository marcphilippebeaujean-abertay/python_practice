from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)  # don't walk off the end

def minimum_bribes(q):
    num_bribes = {}
    while True:
        any_swaps = False
        for i in range(0, len(q)-1):
            if q[i]>q[i+1]:
                print(f'{q[i]} should swap with {q[i+1]}')
                q[i+1], q[i] = q[i], q[i+1]
                bribes = num_bribes.get(q[i+1], 0) + 1
                if bribes > 2:
                    print("too many swaps for ", q[i+1])
                    return
                num_bribes[q[i+1]] = bribes
                any_swaps = True
        if not any_swaps:
            print(sum(num_bribes.values()))
            break


q = [int(s) for s in "5 1 2 3 7 8 6 4".split()]
q.sort()
print(*q, sep=(' '))
index = binary_search(q, 20)
print(index)