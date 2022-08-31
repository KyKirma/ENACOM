import matplotlib.pyplot as plt
import numpy as np

def grad(x1, x2):  
    gx1 = 2*x1 - 2
    gx2 = 4*x2
    
    return [gx1, gx2]


def fun_x(x1, x2):
    return ((x1 - 1) ** 2) + (2 * (x2**2))


#x1, x1 = -10 < x1, x2 < 10
x1 = np.linspace(-10, 10, num = 100)
x2 = np.linspace(-10, 10, num = 100)

x1, x2 = np.meshgrid(x1,x2)
#função: min f(x1, x2) = (x1 - 1)² + 2x2²


#pt 1
#plotar a função principal
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x1, x2, fun_x(grad(x1,x2)[0], grad(x1,x2)[1]), cmap='viridis')
ax.set_xlabel('X1')
ax.set_ylabel('X2')

plt.show()


