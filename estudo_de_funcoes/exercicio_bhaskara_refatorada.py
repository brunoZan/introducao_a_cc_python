import math

def main():
	a = float(input("digite o valor de A: "))
	b = float(input("digite o valor de B: "))
	c = float(input("digite o valor de C: "))
	imprime_raizes(a, b, c)


def delta_calcula(a, b, c):
	return b ** 2 - 4 * a * c

def imprime_raizes(a, b, c):
	delta = delta_calcula(a, b, c)
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
main()
