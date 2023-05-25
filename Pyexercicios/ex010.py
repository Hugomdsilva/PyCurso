# Meu Código
import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
requisicao_dic = requisicao.json()

US = float(requisicao_dic["USDBRL"]["bid"])
RS = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = RS / US
print('Com R${:.2f} você pode comprar U${:.2f}'.format(RS,dolar))

# Código da Aula
# real = float(input('Quanto dinheiro você tem na carteira?R$ '))
# dolar = real / 3.27
# print('Com R${:.2f} você pode comprar U${:.2f}'.format(real,dolar))
