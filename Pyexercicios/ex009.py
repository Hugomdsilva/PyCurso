from simple_colors import *

from Color import color

n = int(input('Digite um número para ver sua tabuada: '))
print(color.BOLD, '_____' * 10, color.END)
c = 0
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
#print('{} x  {} = {} '.format(n,1,n*1))
#print('{} x  {} = {} '.format(n,2,n*2))
#print('{} x  {} = {} '.format(n,3,n*3))
#print('{} x  {} = {} '.format(n,4,n*4))
#print('{} x  {} = {} '.format(n,5,n*5))
#print('{} x  {} = {} '.format(n,6,n*6))
#print('{} x  {} = {} '.format(n,7,n*7))
#print('{} x  {} = {} '.format(n,8,n*8))
#print('{} x  {} = {} '.format(n,9,n*9))
#print('{} x  {} = {} '.format(n,1,n*10))
print(color.BOLD, '_____' * 10, color.END)