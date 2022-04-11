# estrutura para armazenar os dados dos produtos
class tprod:
  cod = 0
  nome=''
  preco=0.0
 
 # funcao que retorna o preco do produto
 def retpreco(c, lprod):
  for i in range(len(lprod):
    if lprod[i].cod==c:
      return lprod[i].preco
  return -1 # se nao encontrar o código na lista retorna 0

# funcao para retornar o nome do produto
def retnome(cod, lprod):
  for i in range(len(lprod)):
    if lprod[i].cod==cod:
      return lprod[i].nome
  return 'Produto não cadastrado' #return caso o produto nao for encontrado

# insere uma estrutura do tipo produto que seria o (p) na lista, altera automaticamente a lista que sera passada na chamada
def cadprod(p, lista):
  lista.append(p)
  
def insereprod(lista):
  while True:
    p=tprod()
    p.cod=int(input('Código: '))
    if p.cod==0:
      break
    if retpreco(p.cod, lista)!=1 # para verificar se o codigo ja foi cadastrado
      print('Código já cadastrado.) # pois se o preco for igual a 0 o produto nao existe
      continue
    p.nome=input('Nome: ")
    p.preco=float(input('Preço: '))
    cadprod(p, lista) #chama a funcao de cadastro

def carregarprod(lista):
  f=open(
