""" Given an array of integers, return a new array such that each
element at index i of the new array is the product of all the numbers
in the original array except the one at i.
"""

from microbench import MicroBench
import pandas

basic_bench = MicroBench()

@basic_bench
def calculate_products(array):

    products = []
    prod_prev = 1

    for i, e in enumerate(array):

        for j, p in enumerate(products):

            products[j] = products[j] * e

        products.append(prod_prev)

        prod_prev = prod_prev * e

    return products


def calculate_products_alt(array):

    group_product = 1
    products = []

    if len(array) == 1:
        group_product = array[0]
        products = [1]

        return (products, group_product)

    if len(array) >= 2:
        array_len = len(array)
        array_split = array_len // 2

        products_a, group_product_a = (
            calculate_products_alt(array[0:array_split]))

        products_b, group_product_b = (
            calculate_products_alt(array[array_split:array_len]))

        group_product = group_product_a * group_product_b

        for i, e in enumerate(products_a):
            products_a[i] = products_a[i] * group_product_b

        for i, e in enumerate(products_b):
            products_b[i] = products_b[i] * group_product_a

        products.extend(products_a)
        products.extend(products_b)

        return (products, group_product)


@basic_bench
def product_wrap_1(array):
    products_list, _ = calculate_products_alt(array)
    return products_list


array = list(range(1, 60))

products_func = calculate_products(array)

products_test = product_wrap_1(array)

results = pandas.read_json(basic_bench.outfile.getvalue(), lines=True)

results['time'] = results['finish_time'] - results['start_time']

print(results)












