p = float(input('Qual o preço do produto? R$'))
novo = p - (p * (5 / 100))
print('O produto que custava R${}, na promoção com desconto de 5% vai custar {:.2f}'.format(p, novo))