titulo = "Media de quatro valores"
print(f'{titulo:^30}')

x = float(input('Entre com o valor de x: '))
y = float(input('Entre com o valor de y: '))
a = float(input('Entre com o valor de a: '))
z = float(input('Entre com o valor de z: '))
media = (x+y+a+z)/4
print("O valor de x é", x, "!")
print('O valor de y é', y)
print("O valor de x é", a, "!")
print('O valor de y é', z)
print('A media dos valores é', round(media, 3))