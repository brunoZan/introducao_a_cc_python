import math
a = float(input("digite o valor de A: "))
b = float(input("digite o valor de B: "))
c = float(input("digite o valor de C: "))


delta = b ** 2 - 4 * a * c

if delta == 0:
	raiz1 = (-b + math.sqrt(delta)) / (2 * a)
	print("A unica raiz é:", raiz1)
else:
	if delta < 0:
		print("Esta equação nao possui raizes reais")
	else:
		raiz1 = (-b + math.sqrt(delta)) / (2 * a)
		raiz2 = (-b - math.sqrt(delta)) / (2 * a)
		print("Primeira raizz:", raiz1 )
		print("Segunda raizz:", raiz2 )


"""
se o DELTA forr menor que 0 entao  inprimir "A equação nao possui raizes reais"

se o DELTA forr igual a 0 entao  inprimir "A equação possui: raiz"

se o DELTA forr maior que 0 entao  inprimir "A equação possui duas raizes reais"
"""