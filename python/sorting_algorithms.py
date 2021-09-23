import argparse
import time
import random
import sys
import math
from functools import wraps

from heap_util import left_heap_child, right_heap_child, is_heap, visualize_heap

iterations = 1
max_int = 20#sys.maxsize
max_time = 5

# Utility functions

def _is_sorted(l):
    for i, value in enumerate(l[:-1]):
        if value > l[i+1]:
            return False
    return True

def _random_list(n):
    return [random.randint(0, max_int) for i in range(n)]

def copy_list(f):
    @wraps(f)
    def inner(l):
        l = l[:]
        return f(l)
    return inner

def work_on_sublist(f):
    @wraps(f)
    def inner(l, start_i=None, end_i=None, copy=True):
        if copy:
            l = l[:]
        if start_i is None:
            start_i = 0
        if end_i is None:
            end_i = len(l)
        return f(l, start_i, end_i, copy)
    return inner

# Sorting algorithms

@copy_list
def bogosort(l):
    # Shuffle l until it is sorted
    while not _is_sorted(l):
        random.shuffle(l)
    return l

@copy_list
def bubblesort(l):
    while True:
        swapped = False

        for i in range(len(l) - 1):
            # If l[i] and l[i+1] are not in order, swap them
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swapped = True

        # Repeat until we go through the whole list without swapping anything
        if not swapped:
            break
    return l

@copy_list
def insertionsort(l):
    for sorted_i in range(len(l)):
        value = l[sorted_i]

        # Find the index of the first element in the sorted part of the list greater than value
        i = 0
        while i < sorted_i and l[i] <= value:
            i += 1
        # Insert value into the sorted part of the list
        for j in range(i, sorted_i+1):
            value, l[j] = l[j], value
    return l

@copy_list
def selectionsort(l):
    for sorted_i in range(len(l)):
        # Find the index of the smallest value in the unsorted part of the list
        min_index, min_value = sorted_i, l[sorted_i]
        for j in range(sorted_i, len(l)):
            value = l[j]
            if value < min_value:
                min_index, min_value = j, value
        # Append the smallest value found to the end of the sorted part of the list
        l[sorted_i], l[min_index] = l[min_index], l[sorted_i]
    return l

@work_on_sublist
def mergesort(l, start_i, end_i, copy):
    if end_i - start_i > 1:
        # Divide l into halves and recursively mergesort each
        mid = (start_i + end_i) // 2
        mergesort(l, start_i, mid, False)
        mergesort(l, mid, end_i, False)

        # Merge the two halves together in sorted order
        i1 = start_i
        i2 = mid
        merged = list()
        while i1 < mid or i2 < end_i:
            if i1 < mid and i2 < end_i:
                if l[i2] < l[i1]:
                    merged.append(l[i2])
                    i2 += 1
                else:
                    merged.append(l[i1])
                    i1 += 1
            elif i1 < mid:
                merged.append(l[i1])
                i1 += 1
            else:
                merged.append(l[i2])
                i2 += 1
        l[start_i:end_i] = merged
        return merged

    return l

@work_on_sublist
def quicksort(l, start_i, end_i, copy):
    if end_i - start_i > 1:
        # Choose the first element of the list as a pivot
        pivot = l[start_i]
        # Partition the array to put all elements less than the pivot before all items greater than it
        i1 = start_i + 1
        i2 = end_i - 1
        while i1 < i2:
            if l[i1] > pivot and l[i2] < pivot:
                l[i1], l[i2] = l[i2], l[i1]
                i1 += 1
                i2 -= 1
            elif l[i1] > pivot:
                l[i1], l[i2] = l[i2], l[i1]
                i2 -= 1
            elif l[i2] < pivot:
                l[i1], l[i2] = l[i2], l[i1]
                i1 += 1
            else:
                i1 += 1
                i2 -= 1
        # Move the pivot  between the two partitions
        mid = i1
        if l[mid] > pivot:
            mid -= 1
        l[start_i], l[mid] = l[mid], pivot
        # Recursively apply to the partitions
        if mid - start_i > 1:
            quicksort(l, start_i, mid, False)
        if end_i - mid > 1:
            quicksort(l, mid + 1, end_i, False)

    return l


def max_heapify(l, i, heap_size):
    left_child = left_heap_child(i)
    right_child = right_heap_child(i)
    max_i, max_value = i, l[i]
    # If the left or right child of l[i] is larger than it, exchange them
    if left_child < heap_size and l[left_child] > max_value:
        max_i, max_value = left_child, l[left_child]
    if right_child < heap_size and l[right_child] > max_value:
        max_i, max_value = right_child, l[right_child]
    if max_i != i:
        l[i], l[max_i] = l[max_i], l[i]
        # Then max_heapify the subheap rooted at that child
        max_heapify(l, max_i, heap_size)

@copy_list
def heapsort(l):
    length = len(l)
    # Turn l into a max heap
    for i in range(math.floor(length / 2), -1, -1):
        max_heapify(l, i, length)
    # Put the current root of the heap (the largest element) at the end of the lieft
    # Then restore the heap
    for heap_size in range(length, 0, -1):
        l[heap_size-1], l[0] = l[0], l[heap_size-1]
        max_heapify(l, 0, heap_size-1)

    return l

algorithms = [bubblesort, insertionsort, selectionsort, mergesort, quicksort, heapsort]
joke_algorithms = [bogosort]

# Test methods

def test_algorithms():
    l_small = _random_list(10)
    l = _random_list(1000)
    assert _is_sorted(sorted(l))

    for algorithm in algorithms:
        sorted_l = algorithm(l_small)
        status = 'succeeded' if _is_sorted(sorted_l) else 'FAILED'
        print(f'{algorithm.__name__}: Sorting {status}')

    # for algorithm in joke_algorithms:
    #     sorted_l = algorithm(l_small)
    #     status = 'succeeded' if _is_sorted(sorted_l) else 'FAILED'
    #     print(f'{algorithm.__name__}: Sorting {status}')

def time_algorithms():
    lists = dict()

    for algorithm in algorithms:# + joke_algorithms:
        previous = None
        n = 8
        while True:
            if n not in lists:
                lists[n] = _random_list(n)
            l = lists[n]
            total_time = 0
            for iteration in range(iterations):
                start = time.time()
                algorithm(l)
                total_time += time.time() - start
            avg_time = total_time / iterations
            msg = f'{algorithm.__name__} took {avg_time:.6f}s to sort {n} elements'
            if previous is not None:
                ratio = avg_time / previous
                msg = f'{msg} (ratio: {ratio:.3f})'
            print(msg)
            previous = avg_time
            if avg_time > max_time:
                break
            n *= 2
        print()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['test', 'time'])
    args = parser.parse_args()

    if args.mode == 'test':
        test_algorithms()
    else:
        time_algorithms()

if __name__ == '__main__':
    main()