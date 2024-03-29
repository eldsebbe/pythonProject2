import numpy as np

def gaussElim(a, b):
    n = len(b)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                lem = a[i, k] / a[k, k]
                a[i,k+1:n] = a[i,k+1:n] - lem * a[k, k + 1:n]
                b[i] = b[i] - lem * b[k]
    for k in range(n - 1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k + 1:n], b[k + 1:n])) / a[k, k]

    return b




