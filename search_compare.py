#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 Assignment 4, Part 1."""

from __future__ import division
import random
import time

def list_generate(xrange_size, list_size):
    """Generates 100 random lists for test data.

    Args:
        xrange_size (int): Specifies the range of numbers.
        list_size (int): Specifies the number of list elements.

    Returns:
        random_list (list): 100 lists of randomly generated lists.
    """
    counter = 0
    random_list = []
    while counter < 100:
        random_list.append(random.sample(xrange(xrange_size), list_size))
        counter += 1
    return random_list

def sequential_search(a_list, item):
    """Searches a list sequentially.

    Args:
        a_list (list): The list to be searched.
        item (int): The item to be found.

    Returns:
        found (bool): Whether the item was found.
        searchtime (float): Time to execute function.
    """
    pos = 0
    found = False
    start = time.time()

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    end = time.time()
    searchtime = end - start

    return found, searchtime

def ordered_sequential_search(a_list, item):
    """Searches a an ordered list.

    Args:
        a_list (list): The list to be searched.
        item (int): The item to be found.

    Returns:
        found (bool): Whether the item was found.
        searchtime (float): Time to execute function.
    """
    pos = 0
    found = False
    stop = False
    start = time.time()

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1

    end = time.time()
    searchtime = end - start

    return found, searchtime

def binary_search_iterative(a_list, item):
    """Runs a binary search on a list.

    Args:
        a_list (list): The list to be searched.
        item (int): The item to be found.

    Returns:
        found (bool): Whether the item was found.
        searchtime (float): Time to execute function.
    """
    first = 0
    last = len(a_list) - 1
    found = False
    start = time.time()

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    searchtime = end - start

    return found, searchtime

def binary_search_recursive(a_list, item):
    """Runs a recursive binary search on a list.

    Args:
        a_list (list): The list to be searched.
        item (int): The item to be found.

    Returns:
        found (bool): Whether the item was found.
        start-end (float): Time to execute function.
    """

    start = time.time()

    if len(a_list) == 0:
        end = time.time()
        return False, (end - start)
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        end = time.time()
        return True, (end - start)
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)

def displayResults(search_func, elements):
    """Displays results of search tests."""
    # Generate test data - 100 lists of stated elements
    test = list_generate(elements, elements)
    # If search other than sequential, order the lists
    if search_func == ordered_sequential_search or binary_search_iterative or \
            binary_search_recursive:
        counter = 0
        for i in test:
            test[counter].sort()
            counter += 1
    results = []
    # Run search test and compile searchtimes into list, then calculate average
    for i in test:
        results.append((search_func(test, -1))[1])
    average = sum(results) / len(results)
    # Format function names for nicer results printing
    if search_func == sequential_search:
        search_func = 'Sequential Search'
    elif search_func == ordered_sequential_search:
        search_func = 'Ordered Sequential Search'
    elif search_func == binary_search_iterative:
        search_func = 'Binary Search Iterative'
    elif search_func == binary_search_recursive:
        search_func = 'Binary Search Recursive'
    # Print results
    print 'On average, {} took{:10.7f} seconds to run on 100 ' \
          'lists of {} elements'.format(search_func, average, elements)

def main():
    displayResults(sequential_search, 500)
    displayResults(sequential_search, 1000)
    displayResults(sequential_search, 10000)
    displayResults(ordered_sequential_search, 500)
    displayResults(ordered_sequential_search, 1000)
    displayResults(ordered_sequential_search, 10000)
    displayResults(binary_search_iterative, 500)
    displayResults(binary_search_iterative, 1000)
    displayResults(binary_search_iterative, 10000)
    displayResults(binary_search_recursive, 500)
    displayResults(binary_search_recursive, 1000)
    displayResults(binary_search_recursive, 10000)

if __name__ == "__main__":
    main()