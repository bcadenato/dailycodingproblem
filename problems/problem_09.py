"""Daily Coding Problem 09.
Given a list of integers, write a function that returns the largest sum
of non-adjacent numbers. Numbers can be 0 or negative."""

import logging
import sys

def get_sets(a):
    """Returns an array with all the legal sums"""

    logging.debug("Calling get_sets with %s", str(a))
    a_len = len(a)

    if a_len == 3:
        s = [[a[0]], [a[1]], [a[2]], [a[0], a[2]]]
        logging.debug(
           "Exiting get_sets:\n Array %s\n Return value %s",
           a, s)
        return s

    if a_len == 2:
        s = [[a[0]], [a[1]]]
        logging.debug(
           "Exiting get_sets:\n Array %s\n Return value %s",
           a, s)
        return s

    if a_len == 1:
        s = [[a[0]]]
        logging.debug(
           "Exiting get_sets:\n Array %s\n Return value %s",
           a, s)
        return s

    s = []

    e1 = get_sets(a[2:])

    for i in e1:
        i.insert(0, a[0])
        s.append(i)

    e2 = get_sets(a[3:])

    for i in e2:
        i.insert(0, a[1])
        s.append(i)

    logging.debug(
       "Exiting get_sets:\n Array %s\n Return value %s",
       a, s)
    return s


def get_largest_sum(a):
    """Returns the array that provides the largest possible sum"""

    s = get_sets(a)

    t_sum = 0
    t = []

    for a in s:
        e_s = sum(a)
        if e_s > t_sum:
            t_sum = e_s
            t = a

    return t

logging.basicConfig(
    filename = "logs/problem-09.log",
    level = logging.ERROR)

a = [int(x) for x in sys.argv[1:]]

print(f"Input array: {a}")

s = get_largest_sum(a)

print(f"Largest sum sub-array: {s}")
