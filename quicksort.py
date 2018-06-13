'''
A file contains all of the integers between 1 and 10,000 (inclusive, with no repeats)
in unsorted order. The integer in the ith row of the file gives you the ith entry of an input
array.

Your task is to compute the total number of comparisons used to sort the given input file by
QuickSort. As you know, the number of comparisons depends on which elements are chosen as
pivots, so we'll ask you to explore three different pivoting rules.

Pivots:
1. First element
2. Last element (same as 1 but just before recursive call, swap last element with first)
3. "Median of three" (e.g. in [8,2,4,5,7,1], the median of [8,4,1] is used: 4)

'''
import math
import statistics


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def choose_pivot(arr, length):
    # Pivot is 1st element
    # return arr
    # Pivot is last element
    # return swap(arr, 0, length - 1)
    # Pivot is median of 3 elements
    mid_idx = int(math.ceil(length / 2)) - 1
    li = [arr[0], arr[mid_idx], arr[length - 1]]
    med = statistics.median(li)

    if med == li[1]:
        return swap(arr, 0, mid_idx)
    elif med == li[2]:
        return swap(arr, 0, length - 1)
    else:
        return arr


def partition(arr, length):
    pivot = arr[0]
    idx_2 = 1
    for idx, val in enumerate(arr):
        j = idx + 1

        # element is less than pivot: swap element with i, increment i
        if (j < length and arr[j] < pivot):
            arr = swap(arr, idx_2, j)
            idx_2 += 1

    # swap pivot with arr[i - 1]
    pvt_idx = idx_2 - 1
    arr = swap(arr, pvt_idx, 0)
    return arr, pvt_idx


def quicksort(arr, length):
    if length <= 1:
        return arr, 0

    # to count total comparisons, add length - 1 to count each time quicksort is called
    count = length - 1

    arr = choose_pivot(arr, length)
    arr, pvt_idx = partition(arr, length)

    # recursively sort around pivot element
    first = arr[:pvt_idx]
    second = arr[pvt_idx + 1:]
    a_out, a_count = quicksort(first, len(first))
    b_out, b_count = quicksort(second, len(second))

    return a_out + [arr[pvt_idx]] + b_out, count + a_count + b_count


# arr = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
f = open('quicksort.txt', 'r')
arr = list(map(int, f.read().splitlines()))

result = quicksort(arr, len(arr))
print('result: ', result)

f.close()
