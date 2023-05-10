import matplotlib.pyplot as plt
import numpy as np

def grad(x1, x2):  
    gx1 = (2*x1) - 2
    gx2 = 4*x2
    
    return np.array([gx1, gx2])

def fun_x(x1, x2):
    return pow((x1 - 1), 2) + (2 * pow(x2, 2))

#x1, x1 = -10 < x1, x2 < 10
x1 = np.linspace(-10, 10, num = 100)
x2 = np.linspace(-10, 10, num = 100)

x1, x2 = np.meshgrid(x1, x2)

#ponto inicial
X1, X2 = 10, 10

x2k = [10]
y2k = [10]

#algoritmo
i = 0
while (i < 100):
    gk = grad(X1, X2)
    norma = np.sqrt(pow(gk[0], 2) + pow(gk[1], 2))
    
    if norma <= 0.01:
        break

    print(norma)
    dk = (gk/norma) * (-1)
    alpha = ((dk[0] - (X1 * dk[0])) - (2 * X2 * dk[1])) / (pow(dk[0], 2) + (2 * pow(dk[1], 2)))

    X1 = X1 + (alpha * dk[0])
    X2 = X2 + (alpha * dk[1])

    x2k.append(X1)
    y2k.append(X2)
    i = i + 1

    print(i,'//', X1,'//', X2,'//', gk,'//', dk,'//',alpha,'//', norma)
#plotar a função principal

fig = plt.figure(figsize = plt.figaspect(.4))

ax = fig.add_subplot(1, 2, 1)


CS = ax.contour(x1, x2, fun_x(x1, x2), cmap='bone')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.clabel(CS)
ax.plot(1, 0, "ro")
ax.set_title('Curvas de nivel\nFunção Inicial')
plt.plot(x2k, y2k, 'o-', color='red', label='Descida do Gradiente')
plt.legend()


#EXTRA: função inicial em visualização 3D

ax = fig.add_subplot(1, 2, 2, projection = '3d')

ax.set_xlabel('X1')
ax.set_ylabel('X2')
surf = ax.plot_surface(x1, x2, fun_x(x1, x2), cmap='bone')
ax.plot(x2k, y2k, fun_x(np.asarray(x2k), np.asarray(y2k)), 'o-', color='red', label='Descida do Grandinte')
ax.plot(1, 0, "ro")
ax.set_title('Projeção 3D\nFunção Inicial')
plt.legend()
plt.show()