
#  Funcao: removePalavras
#
#  Parametros:
#    s: string contendo o texto de entrada
#    vs: lista de strings com as palavras a serem removidas
#
#  Descricao:
#    Deve-se remover as palavras de s que estiverem listadas em vs.
#    Ao final, s nao deve conter espacos extras.
#
# Retorno:
#   string s sem as palavras de vs.

def removePalavras(s, vs):
	s=s.split()
	for i in vs:
		while i in s:
			s.remove(i)
	return ' '.join(s)
#print(removePalavras("as flores de plastico nao morrem as flores vao curar esta", ["as", "nao", "esta"]))
#  Funcao: pagsResposta
#
# Parametros:
#   paginas: lista de strings cada uma representando uma pagina
#   termosBusca: lista de strings com os termos a serem buscados
#
# Descricao:
#	Deve verificar se cada página em paginas contém todos os termos
#	de busca em termosBusca. Se a paginas[i] contiver todos os termos
#	então deve-se atribuir 1 para resp[i] e 0 caso não contenha pelo
#	menus um dos termos de busca.
#
# Retorno:
#   lista a ser preenchida como resposta, de dimensao numPag.

def pagsResposta(palavrasPagina, termosBusca):
	resp=[]
	for i in palavrasPagina:
		s=i.split()
		for a in termosBusca:
			if a not in s:
				match= False
				resp.append(0)
				break
			else:
				match= True
		if match == True:
			resp.append(1)
	return resp
#print(pagsResposta(["cartao postal azul", "carta postal", "azul e a cor do postal"], ["azul", "postal"]))

#  Funcao: linksResposta
#
# Parametros:
#   links: matriz quadrada binária representando links entre as paginas
#   resp: lista obtido apos execucao de pagsResposta
#
# Descricao:
#   Deve-se preencher uma lista numLinks da seguinte maneira: para cada
#   posicao i (0 <= i < numPags), se resp[i] == 1, então numLinks[i] deve conter
#   o numero de links de outras paginas resposta para i. Caso resp[i] == 0,
#   entao numLinks[i] deve ser -1.
#
# Retorno
#   lista numLinks a ser preenchida como resposta, de tamanho numPag

def linksResposta(links,resp):
	numLinks=[]
	for i in range(len(resp)):
		if resp[i]==1:
			linkCount=0
			for a in range(len(resp)):
				if resp[a]==1:
					if links[a][i] == 1:
						linkCount+=1
			numLinks.append(linkCount)
		else:
			numLinks.append(-1)
	return numLinks
#print(linksResposta([[0, 1, 1], [1, 0, 1], [0, 1, 0]], [1, 0, 1]))
