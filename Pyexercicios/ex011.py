from Color import color
print(color.BOLD, '__'*14, color.END)
L = float(input('Largura da parede:'))
A = float(input('Altura da parede'))
m2 = L * A
tinta = m2/2

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m²'.format(L, A, m2))
print('Para pintar sua parede, você precisará de {:.1f}l de tinta'.format(tinta))
print(color.BOLD, '__'*14, color.END)