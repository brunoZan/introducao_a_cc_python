# def computador_escolhe_jogada(n, m)

# def usuario_escolhe_jogada(n, m)

# def partida()

# def campeonato()

# partida
# 	(pode au user o numero de deças e Tiradas)
# 	(verifica quem começa baseado nas Tiradas)
# 	(função: user_começa() ou pc_começa())
	
def computador_escolhe_jogada(n, m):
	if n <= m:
		return n
	else:
		quantia = n % (m + 1) 
	if( quantia > 0):
		return quantia
	return m


