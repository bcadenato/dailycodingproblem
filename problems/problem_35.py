'''
Given an array of strictly the characters 'R', 'G', and 'B', segregate
the values of the array so that all the Rs come first, the Gs come
second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.
'''

def swap_array(array, i, j):
    array[i], array[j] = array[j], array[i]


def arrange_array(array):
    g0 = -1
    g1 = -1
    b0 = -1

    for i, e in enumerate(array):
        if e == 'B':
            if b0 < 0:
                b0 = i

        if e == 'G':
            if g0 >= 0: 
                if b0 >= 0:
                    swap_array(array, b0, i)

                    g1 = b0
                    b0 = b0 + 1
                else:
                    g1 = g1 + 1
            else:
                if b0 >= 0:
                    swap_array(array, b0, i)

                    g0 = b0
                    g1 = b0
                    b0 = b0 + 1
                else:
                    g0 = i
                    g1 = i

        if e == 'R':
            if b0 >= 0:
                if g0 >= 0:
                    swap_array(array, b0, i)
                    swap_array(array, g0, b0)

                    g0 = g0 + 1
                    g1 = g1 + 1
                    b0 = b0 + 1
                else:
                    swap_array(array, b0, i)

                    b0 = b0 + 1
            else:
                if g0 >= 0:
                    swap_array(array, g0, i)

                    g0 = g0 + 1
                    g1 = i

    return array

def arrange_array_2(array):
    idx_low = 0
    idx_mid = 0
    idx_high = len(array) - 1

    while idx_mid < idx_high:
        if array[idx_mid] == 'B':
            swap_array(array, idx_mid, idx_high)
            idx_high -= 1

        if array[idx_mid] == 'R':
            swap_array(array, idx_mid, idx_low)
            idx_low += 1
            idx_mid += 1

        if array[idx_mid] == 'G':
            idx_mid += 1

    return(array)


array_test = ['G', 'B', 'R', 'R', 'B', 'R', 'G']

print(f'Sorting array {array_test} with method 1:')
array_sorted = arrange_array(array_test.copy())
print(array_sorted)

print(f'Sorting array {array_test} with method 2:')
array_sorted_2 = arrange_array_2(array_test.copy())
print(array_sorted_2)













