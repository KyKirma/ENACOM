import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 

def func3d(x):
  x1,x2=x
  return 2*pow(x1,2) + pow(x2,2) + (2*x1*x2) + x - (2*x2) + 3

def grad3d(x):
  x1, x2 = x
  h = 0.01
  h1 = np.array([h, 0.0])
  h2 = np.array([0.0, h])
  z = func3d(x)
  df_dx = (func3d(x+h1)-z)/h
  df_dy = (func3d(x+h2)-z)/h
  return np.array([df_dx, df_dy])

def grad_desc(x,step=0.005):
  x = x - step * grad3d(x)
  return x

x = np.array([np.linspace(-10, 10, num=100), np.linspace(-10, 10, num=100)])
z = func3d(x)

xi = np.array([0.5,0.8])
xs = []
zs = []
for i in range(2):
  zi = func3d(xi)
  xs.append(xi)
  zs.append(z)
  xi = grad_desc(xi)
xs = np.array(xs)
zs = np.array(zs)

ax = plt.axes(projection='3d')
ax.view_init(50,-45)
ax.plot_surface(x[0,:], x[1,:], z, cmap=cm.Spectral)
ax.plot(xs[:,1], xs[1,:], zs, 'o', c = 'b', zorder=100)
plt.axis('off')
plt.show()
