"""Given an array of integers and a number k, where 1 <= k <= length of the
array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3,
we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place
and you do not need to store the results. You can simply print them out as you
compute them."""


def get_maxvals(input_array, k):
    """Returns the  maximum value for every subarray of length k
    in the array input_array
    """
    max_vals = []
    for sub_array in get_arrays(input_array, k):
        max_val = max(sub_array)
        max_vals.append(max_val)

    return max_vals


def get_arrays(input_array, k):
    """Generator to return sub-arrays of length k for an input_array."""
    array_len = len(input_array)
    for i in range(0, (array_len + 1) - k):
        yield input_array[i:i+k]


m = get_maxvals([10, 5, 2, 7, 8, 7], 3)

print(m)
