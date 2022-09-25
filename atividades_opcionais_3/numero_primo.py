n = int(input("Digite um número inteiro: "))
is_primo = 0
counter = 2

while counter < n:
	if n % counter == 0:
		is_primo += 1

	counter += 1

if is_primo >= 1 or n == 1:
	print("nao primo")
else:
	print("primo")