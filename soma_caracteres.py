numero = int(input("digite um sequencia de números: "))

soma_resto = 0

while numero > 0:
	soma_resto += numero % 10
	numero = numero // 10
print(soma_resto)

"""
"""