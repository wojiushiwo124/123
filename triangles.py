# -*- coding: utf-8 -*-
def triangles():
    Y = [1]
    while True:
        yield Y
        Y = [1] + [Y[i] + Y[i + 1] for i in range(len(Y) - 1)] + [1]
