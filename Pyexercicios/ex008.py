m = float(input('Sou especialista em medidas me fale uma distancia em metros e verá que falo a verdade: '))
print('A medida de {}m corresponde a'.format(m))
print('{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(m/1000, m/100, m/10, m*10, m*100, m*1000))