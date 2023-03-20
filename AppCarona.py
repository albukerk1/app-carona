fuelprice = float(input('Preço do litro de combustível:'))
km = float(input('Kilômetros rodados:'))
kml = float(input('Rendimento do automóvel (km/L):'))
num = float(input('Número de pessoas a pagar:'))
total = ((fuelprice*km)/(kml))/num
print('R${:.2f}'.format(total))
