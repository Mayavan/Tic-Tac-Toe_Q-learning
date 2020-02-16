from numpy import *

def comb(a,b):
    c = []
    for i in range(189):
        for j in b:
            c.append(r_[i,j])
    return c