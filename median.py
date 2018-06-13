# input array: [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12] left: 2 right: 12 middle: 10 median: 10 count: 19

# input array: [7, 1, 3, 6, 2, 5, 4, 9, 8] left: 7 right: 8 middle: 2 median: 7 count: 8

# input array: [4, 1, 3, 6, 2, 5] left: 4 right: 5 middle: 3 median: 4 count: 5

# input array: [2, 1, 3] left: 2 right: 3 middle: 1 median: 2 count: 2

# input array: [6, 5] left: 6 right: 5 middle: 6 median: 6 count: 1

# input array: [9, 8] left: 9 right: 8 middle: 9 median: 9 count: 1

# input array: [19, 11, 13, 15, 16, 14, 18, 17, 20, 12] left: 19 right: 12 middle: 16 median: 16 count: 9

# input array: [12, 11, 13, 15, 14] left: 12 right: 14 middle: 13 median: 13 count: 4

# input array: [12, 11] left: 12 right: 11 middle: 12 median: 12 count: 1

# input array: [15, 14] left: 15 right: 14 middle: 15 median: 15 count: 1

# input array: [18, 17, 20, 19] left: 18 right: 19 middle: 17 median: 18 count: 3

# input array: [20, 19] left: 20 right: 19 middle: 20 median: 20 count: 1

# sorted array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# total count: 55

import statistics
import math

arr = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
length = len(arr)

mid_idx = int(math.ceil(length / 2)) - 1
three = [arr[0], arr[mid_idx], arr[length - 1]]
median = statistics.median(three)

if median == three[0]:
    result = three[0]
elif median == three[1]:
    result = three[1]
else:
    result = three[2]


print(three, result)
