#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 Assignment 4, Part 2."""

import random
import time

test_list = random.sample(xrange(10),10)

def list_generate(xrange_size, list_size):
    """Generates a single random list for test data.

    Args:
        xrange_size (int): Specifies the range of numbers.
        list_size (int): Specifies the number of list elements.

    Returns:
        random_list (list): A list of randomly generated integers.
    """
    random_list = random.sample(xrange(xrange_size), list_size)
    return random_list

def insertion_sort(a_list):
    """Insertion sort, base taken from text, timer added."""
    start = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

    end = time.time()
    return start-end

def shell_sort(a_list):
    """"Shell sort, base taken from text, timer added."""
    start = time.time()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2

    end = time.time()
    return start-end

def gap_insertion_sort(a_list, start, gap):
    """Gap insertion sort, base taken from text, necessary for shell_sort
    to function properly.
    """
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value

def python_sort(a_list):
    """Wrapper for Python built-in sort, timer added"""
    start = time.time()

    a_list.sort()

    end = time.time()
    return start-end

def displayResults(sort_func, elements):
    """Displays results of search tests."""
    # Generate test data - a list of stated elements
    test = list_generate(elements, elements)
    # Run sort test, assign time to results variable
    results = sort_func(test)
    # Format function names for nicer results printing
    if sort_func == insertion_sort:
        sort_func = 'Insertion Sort'
    elif sort_func == shell_sort:
        sort_func = 'Shell Sort'
    elif sort_func == python_sort:
        sort_func = 'Python Sort'
    # Print results
    print '{} took{:10.7f} seconds to run on a ' \
          'list of {} elements'.format(sort_func, results, elements)

def main():
    displayResults(insertion_sort, 500)
    displayResults(insertion_sort, 1000)
    displayResults(insertion_sort, 10000)
    displayResults(shell_sort, 500)
    displayResults(shell_sort, 1000)
    displayResults(shell_sort, 10000)
    displayResults(python_sort, 500)
    displayResults(python_sort, 1000)
    displayResults(python_sort, 10000)

if __name__ == "__main__":
    main()