n = int(input("Digite um número inteiro: "))
count = 0
rest = 0

while n > 0:
	rest = n % 10
	n = n // 10
	if (n % 10) == rest:
		count += 1

if count > 0:
	print("sim")
else:
	print("não")
