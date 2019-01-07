import collections

def countTriplets(arr, r):
    nr_of_triplets = 0
    mid_val_dict, third_val_dict = collections.defaultdict(int), collections.defaultdict(int)
    for num in arr:
        if num in third_val_dict:
            nr_of_triplets+=third_val_dict[num]
        if num in mid_val_dict:
            third_val_dict[num*r]+=mid_val_dict[num]
        mid_val_dict[num*r]+=1
    return nr_of_triplets

def countSwaps(a):
    is_sorted = False
    swaps = 0
    while is_sorted is False:
        is_sorted = True
        for i in range(0, len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False
                swaps+=1
    print(f'{swaps}, {a[0]}, {a[len(a)-1]}')

arr = [int(s) for s in "1 2 4 2".split()]
countSwaps(arr)