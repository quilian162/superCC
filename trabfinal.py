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
      continue # se nao existir, volta ao comeco do laço
    p.nome=input('Nome: ")
    p.preco=float(input('Preço: '))
    cadprod(p, lista) #chama a funcao de cadastro

def carregarprod(lista):
  f=open('produtos.txt','a+')
  f.seek(0)
  llin=f.readlines()
  for l i llin:
    prod=l.split(',')
    p=tprod()
    p.cod=int(prod[0])
    p.nome=prod[1]
    p.preco=float(prod[2][:-'])
    lista.append(p)
  f.close()
                          
def armzprod(lista)
  f=open('produtos.txt','w')
  for i in range(len(lista)):
    f.write(str(lista[i].cod)+','+lista[i].nome+','+str(lista[i].preco)+'\n')
# inserindo manualmente os produtos na lista para utilizar a funcao que pede os produtos pelo teclado

#Main do Programa
produtos[]
carregarprod(produtos)
insereprod(produtos)                  
armzprod(produtos)
x = 'Sim'
while x == 'Sim':
  total=0
  cod=int(input('Código: '))
  while cod!=0
    psr=0
    qnt=int(input('Quantidade: '))
    print(retnome(cod, produtos),' ',end='')
    pr=retpreco(cod,produtos)
    if pr==-1:
      print('Produto não cadastrado')
    else:
      psr=pr*qt
      total+=pr*qt
      print('R$ {:.2f} , Valor Parcial: R$ {:.2f} '.format(psr,total))
    cod=int(input('Código: '))
  print('Valor final: %.2f'%total)
  x=input('Continuar? (X(sim)/Y(nao): ').upper()
