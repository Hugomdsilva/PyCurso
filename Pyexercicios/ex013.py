s = float(input('Qual é o salário do funcionario? R$'))
aumento = s + (s * 15/100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(s, aumento))