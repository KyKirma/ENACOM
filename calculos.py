import matplotlib.pyplot as plt
import numpy as np

def dk (grad, x1, x2):
    return (grad/np.sqrt(pow(x1, 2) + pow(x2, 2)) * -1)

def grad(x1, x2):  
    gx1 = 2*x1 - 2
    gx2 = 4*x2
    
    return [gx1, gx2]

d = dk(grad(10, 10), 10, 10)
print(d)