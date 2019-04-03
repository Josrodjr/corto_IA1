# Jose Rodolfo Perez 16056

import numpy as np

# derivada de J y debe devolver un vector Theta y tiene los mismos params que lienar cost.

def deriv_punto(theta, X, y):
    # hacer la derivada en un punto
    # obtener hipotesis
    h = np.matmul(X, theta)
    # obtener m
    m, n = X.shape
    # list of derivatives
    dv = []
    # iterate over the number of values
    for i in range(m):
        deriv = ((y**i) - h[i]**i)*n[i]
        deriv = (1/m[i])*deriv
        dv.append(deriv)
    return dv