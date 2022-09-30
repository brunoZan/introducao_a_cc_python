def ft(n):
	result = 1
	i = 1
	while i <= n:
		result *= i
		i += 1
	return result

def cfbn(x, y):
	return ft(x) // (ft(y) * ft(x - y))

print("canculando Coeficiente binomial: ")
x = int(input("valor do numerador X:"))
y = int(input("valor do demominador Y:"))

print("Coeficiente binomial: ", cfbn(x, y))

def testes_coeficientes_binomial():
	if cfbn(5, 3) == 10:
		print("funciona pra esses valores")
	else:
		print("não funciona pra esses valores")
	if cfbn(10, 10) == 1:
		print("funciona pra esses valores")
	else:
		print("nao funciona pra esses valores")
