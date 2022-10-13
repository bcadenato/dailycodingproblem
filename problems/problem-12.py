def get_climbing_ways(n, l):

    w = []
    m = [i for i in l if i <= n]

    for i in m:
        if i == n:
            w.append([i])
        else:
            x = get_climbing_ways(n - i, m)

            for j in x:
                j.insert(0, i)
                w.append(j)

    return w

x = get_climbing_ways(4, [1, 2])

print(x)
