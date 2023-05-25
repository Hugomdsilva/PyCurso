#Meu código
#n = int(input('Escreva um numero e te mostrarei os segredos dele:'))
#print('Seu numero mais ele mesmo é igual à {}! \n Esse numero mais ele mesmo mais ele mesmo é igual à {}!'.format(n*2,n*3))
#print('A raiz do seu numero é {:.3f}'.format(n**(1/2)))

#Código do prof
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}'.format(n,d))
print('o triplo de {} vale {}.\n A raiz de {} é igual à {:.2f}.'.format(n, t, n, r))