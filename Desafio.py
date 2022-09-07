import matplotlib.pyplot as plt
import numpy as np
import math

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

x2k = []
y2k = []

i = 0
while (i < 100):
    gk = grad(X1, X2)
    norma = math.sqrt(pow(gk[0], 2) + pow(gk[1], 2))
    
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


#pt 1
#plotar a função principal
fig, ax = plt.subplots()

ax.contour(x1, x2, fun_x(x1, x2))
plt.plot(x2k, y2k, 'o-', color='purple', label='Descida do Gradiente')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.plot(1, 0, "ro")
ax.set_title('Curvas de nivel\nFunção Inicial')

plt.show()