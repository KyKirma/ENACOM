import matplotlib.pyplot as plt
import numpy as np

def grad(x1, x2):  
    gx1 = 2*x1 - 2
    gx2 = 4*x2
    
    return [gx1, gx2]

def fun_x(x1, x2):
    return pow((x1 - 1), 2) + (2 * pow(x2, 2))

#x1, x1 = -10 < x1, x2 < 10
x1 = np.linspace(-10, 10, num = 100)
x2 = np.linspace(-10, 10, num = 100)

#ponto inicial
Xk = [10, 10]
i = 0
while (i < 10):
    gk = grad(Xk[0], Xk[1])
    dk = (gk/np.sqrt(pow(Xk[0], 2) + pow(Xk[1], 2)) * -1)
    alpha = (dk[0] - Xk[0] * dk[0]) - (2 * Xk[1] * dk[1]) / pow(dk[0], 2) + (2 * pow(dk[1], 2))
    
    Xk = Xk + alpha * dk
    i = i + 1
    print(i,'//', Xk[0],'//', Xk[1],'//', gk,'//', dk,'//', alpha)

x1, x2 = np.meshgrid(x1, x2)

