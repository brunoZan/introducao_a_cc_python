n = int(input("Digite um número inteiro: "))
count = 0

while n > 0:
	count = n % 10 + count
	n = n // 10

print(count)