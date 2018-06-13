## Synopsis
A file contains all of the integers between 1 and 10,000 (inclusive, with no repeats)
in unsorted order. The integer in the ith row of the file gives the ith entry of an input
array.

The task is to compute the total number of comparisons used to sort the given input file by
QuickSort. Recall the number of comparisons depends on which elements are chosen as
pivots, so in this problem we'll solve for the total comparisons using three different pivoting rules.

Pivots:
1. First element
2. Last element (same as 1 but just before recursive call, swap last element with first)
3. "Median of three" (e.g. in [8,2,4,5,7,1], the median of [8,4,1] is used: 4)

## Motivation
QuickSort introduced the benefits of randomization in algorithm writing and gave us the most efficient sorting algorithm we have reviewed thus far with **O(nlogn)** time.

## Acknowledgements

This algorithm is part of the Stanford University Algorithms 4-Course Specialization on Coursera, instructed by Tim Roughgarden.
