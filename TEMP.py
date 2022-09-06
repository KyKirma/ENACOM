
#pt 1
#plotar a função principal

fig, ax = plt.subplots()

ax.contour(x1, x2, fun_x(x1, x2))
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.plot(1, 0, "ro")
ax.set_title('Curvas de nivel\nFunção Inicial')

plt.show()