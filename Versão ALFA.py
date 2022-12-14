import matplotlib.pyplot as plt
import numpy as np

def dk (grad, x1, x2):
    return (grad/np.sqrt(pow(x1, 2) + pow(x2, 2)) * -1)

def grad(x1, x2):  
    gx1 = 2*x1 - 2
    gx2 = 4*x2
    
    return [gx1, gx2]

#função: min f(x1, x2) = (x1 - 1)² + 2x2²
def fun_x(x1, x2):
    return ((x1 - 1) ** 2) + (2 * (x2**2))



#x1, x1 = -10 < x1, x2 < 10
x1 = np.linspace(-10, 10, num = 100)
x2 = np.linspace(-10, 10, num = 100)

x1, x2 = np.meshgrid(x1, x2)

#pt 1
#plotar a função principal em curvas de nivel

fig = plt.figure(figsize = plt.figaspect(.4))

ax = fig.add_subplot(1, 2, 1)

ax.contour(x1, x2, fun_x(x1, x2))
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.plot(1, 0, "ro")
ax.set_title('Curvas de nivel\nFunção Inicial')
ax.quiver(x1, x2, fun_x(x1, x2), 10, 10)

#EXTRA: função inicial em visualização 3D

ax = fig.add_subplot(1, 2, 2, projection = '3d')

ax.set_xlabel('X1')
ax.set_ylabel('X2')
surf = ax.plot_surface(x1, x2, fun_x(x1, x2), cmap='coolwarm')
ax.set_title('Projeção 3D\nFunção Inicial')



plt.show()


#pt 1
#plotar a função principal
fig, ax = plt.subplots()

ax.contour(x1, x2, fun_x(x1, x2))
plt.plot(x2k, y2k, 'o-', color='red', label='Descida do Gradiente')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.plot(1, 0, "ro")
ax.set_title('Curvas de nivel\nFunção Inicial')
plt.legend()
plt.show()