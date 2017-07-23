#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright 2010-2017 Prof. Dr. Ruben Carlo Benante
# Autor: Ruben Carlo Benante <dr.beco@gmail.com>
# Licensa GPL - Software livre
# Ninguém deve ser restringido ao usar um software. Há 4 direitos que todo usuário deve ter:
# Direito número 1: A liberdade de usar o software para qualquer objetivo,
# Direito número 2: A liberdadede mudar o software para se adequar aos seus propósitos,
# Direito número 3: A liberdade de compartilhar o software com seus amigos e vizinhos,
# Direito número 4: A liberdade de compartilhar as mudanças que você fez.
# Deveres são todos relacionados a manter que software livre continue livre.
# Na licensa aplicada a este software o autor esclarece que:
# Um colaborador não pode patentear parte de sua colaboração para depois cobrá-la
# O nome do autor principal deve ser mantido. É esta sua única forma de valorizar seu trabalho.
# Nomes de colaboradores podem ser adicionados abaixo.
# O nome do programa deve ser mantido.
#
# Este é o programa rubikeco.py, fonte em python, para analisar uma solução para o cubo mágico

from copy import deepcopy
from random import randint
from time import time

up=0; down=1; front=2; back=3; right=4; left=5;
achou = 0; nos = 0;

def imprime(cubo):
  for f in range(6):
    if f==up:
      print("up:")
    elif f==down:
      print("down:")
    elif f==front:
      print("front")
    elif f==back:
      print("back")
    elif f==right:
      print("right")
    else:
      print("left")
    for p in range(9):
      if p%3==0 and p!=0:
        print()
      print(cubo[f][p], end='')
    print("\n")

def u(c): #rotacao up horario
  fu=c[up][:]    #face up    = white
  fd=c[down][:]  #face down  = yellow - nao muda
  ff=c[front][:] #face front = red
  fb=c[back][:]  #face back  = orange
  fr=c[right][:] #face right = blue
  fl=c[left][:]  #face left  = green
  #up
  c[up][0]=fu[6]
  c[up][1]=fu[3]
  c[up][2]=fu[0]
  c[up][3]=fu[7]
  c[up][4]=fu[4]
  c[up][5]=fu[1]
  c[up][6]=fu[8]
  c[up][7]=fu[5]
  c[up][8]=fu[2]
  #down   #nada muda
  #front
  c[front][0]=fr[0]
  c[front][1]=fr[1]
  c[front][2]=fr[2]
  #back
  c[back][0]=fl[0]
  c[back][1]=fl[1]
  c[back][2]=fl[2]
  #right
  c[right][0]=fb[0]
  c[right][1]=fb[1]
  c[right][2]=fb[2]
  #left
  c[left][0]=ff[0]
  c[left][1]=ff[1]
  c[left][2]=ff[2]

def ui(c): #rotacao up anti-horario
  u(c)
  u(c)
  u(c)

def d(c): #rotacao down horario
  fu=c[up][:] #up = white -  nao muda
  fd=c[down][:] #down = yellow
  ff=c[front][:] #front = red
  fb=c[back][:] #back = orange
  fr=c[right][:] #right = blue
  fl=c[left][:] #left = green
  #up #nada muda
  #down
  c[down][0]=fd[6]
  c[down][1]=fd[3]
  c[down][2]=fd[0]
  c[down][3]=fd[7]
  c[down][4]=fd[4]
  c[down][5]=fd[1]
  c[down][6]=fd[8]
  c[down][7]=fd[5]
  c[down][8]=fd[2]
  #front
  c[front][6]=fl[6]
  c[front][7]=fl[7]
  c[front][8]=fl[8]
  #back
  c[back][6]=fr[6]
  c[back][7]=fr[7]
  c[back][8]=fr[8]
  #right
  c[right][6]=ff[6]
  c[right][7]=ff[7]
  c[right][8]=ff[8]
  #left
  c[left][6]=fb[6]
  c[left][7]=fb[7]
  c[left][8]=fb[8]

def di(c): #rotacao down anti-horario
  d(c)
  d(c)
  d(c)

def f(c): #rotacao front horario
  fu=c[up][:] #up = white
  fd=c[down][:] #down = yellow
  ff=c[front][:] #front = red
  fb=c[back][:] #back = orange - nao muda
  fr=c[right][:] #right = blue
  fl=c[left][:] #left = green
  #up
  c[up][6]=fl[8]
  c[up][7]=fl[5]
  c[up][8]=fl[2]
  #down
  c[down][0]=fr[6]
  c[down][1]=fr[3]
  c[down][2]=fr[0]
  #front
  c[front][0]=ff[6]
  c[front][1]=ff[3]
  c[front][2]=ff[0]
  c[front][3]=ff[7]
  c[front][4]=ff[4]
  c[front][5]=ff[1]
  c[front][6]=ff[8]
  c[front][7]=ff[5]
  c[front][8]=ff[2]
  #back  #nada muda
  #right
  c[right][0]=fu[6]
  c[right][3]=fu[7]
  c[right][6]=fu[8]
  #left
  c[left][2]=fd[0]
  c[left][5]=fd[1]
  c[left][8]=fd[2]

def fi(c): #rotacao front anti-horario
  f(c)
  f(c)
  f(c)

def b(c): #rotacao back horario
  fu=c[up][:] #up = white
  fd=c[down][:] #down = yellow
  ff=c[front][:] #front = red - nao muda
  fb=c[back][:] #back = orange
  fr=c[right][:] #right = blue
  fl=c[left][:] #left = green
  #up 0
  c[up][0]=fr[2]
  c[up][1]=fr[5]
  c[up][2]=fr[8]
  #down 1
  c[down][6]=fl[0]
  c[down][7]=fl[3]
  c[down][8]=fl[6]
  #front 2 #nada muda
  #back 3
  c[back][0]=fb[6]
  c[back][1]=fb[3]
  c[back][2]=fb[0]
  c[back][3]=fb[7]
  c[back][4]=fb[4]
  c[back][5]=fb[1]
  c[back][6]=fb[8]
  c[back][7]=fb[5]
  c[back][8]=fb[2]
  #right 4
  c[right][2]=fd[8]
  c[right][5]=fd[7]
  c[right][8]=fd[6]
  #left 5
  c[left][0]=fu[2]
  c[left][3]=fu[1]
  c[left][6]=fu[0]

def bi(c): #rotacao back anti-horario
  b(c)
  b(c)
  b(c)

def r(c): #rotacao right horario
  fu=c[up][:]    #face up    = white
  fd=c[down][:]  #face down  = yellow
  ff=c[front][:] #face front = red
  fb=c[back][:]  #face back  = orange
  fr=c[right][:] #face right = blue
  fl=c[left][:]  #face left  = green - nao muda
  #up
  c[up][2]=ff[2]
  c[up][5]=ff[5]
  c[up][8]=ff[8]
  #down
  c[down][8]=fb[0]
  c[down][5]=fb[3]
  c[down][2]=fb[6]
  #front
  c[front][2]=fd[2]
  c[front][5]=fd[5]
  c[front][8]=fd[8]
  #back
  c[back][0]=fu[8]
  c[back][3]=fu[5]
  c[back][6]=fu[2]
  #right
  c[right][0]=fr[6]
  c[right][1]=fr[3]
  c[right][2]=fr[0]
  c[right][3]=fr[7]
  c[right][4]=fr[4]
  c[right][5]=fr[1]
  c[right][6]=fr[8]
  c[right][7]=fr[5]
  c[right][8]=fr[2]
  #left #nada muda

def ri(c): #rotacao right anti-horario
  r(c)
  r(c)
  r(c)

def l(c): #rotacao left horario
  fu=c[up][:]    #face up    = white
  fd=c[down][:]  #face down  = yellow
  ff=c[front][:] #face front = red
  fb=c[back][:]  #face back  = orange
  fr=c[right][:] #face right = blue - nao muda
  fl=c[left][:]  #face left  = green
  #up
  c[up][0]=fb[8]
  c[up][3]=fb[5]
  c[up][6]=fb[2]
  #down
  c[down][0]=ff[0]
  c[down][3]=ff[3]
  c[down][6]=ff[6]
  #front
  c[front][0]=fu[0]
  c[front][3]=fu[3]
  c[front][6]=fu[6]
  #back
  c[back][2]=fd[6]
  c[back][5]=fd[3]
  c[back][8]=fd[0]
  #right #nada muda
  #left
  c[left][0]=fl[6]
  c[left][1]=fl[3]
  c[left][2]=fl[0]
  c[left][3]=fl[7]
  c[left][4]=fl[4]
  c[left][5]=fl[1]
  c[left][6]=fl[8]
  c[left][7]=fl[5]
  c[left][8]=fl[2]

def li(c): #rotacao left anti-horario
  l(c)
  l(c)
  l(c)

#Rotacoes duplas: u2, d2, f2, b2, r2, l2, mx2, my2, mz2, cx2, cy2, cz2
def u2(c): #rotacao dupla de cima
  u(c)
  u(c)

def d2(c): #rotacao dupla de baixo
  d(c)
  d(c)

def f2(c): #rotacao dupla da frente
  f(c)
  f(c)

def b2(c): #rotacao dupla de trás
  b(c)
  b(c)

def r2(c): #rotacao dupla da direita
  r(c)
  r(c)

def l2(c): #rotacao dupla da esquerda
  l(c)
  l(c)

#Rotacoes da camada do meio:
#mx, mxi, my, myi, mz, mzi

#Rotacionar o cubo inteiro
#Cx, Cxi, Cy, Cyi, Cz, Czi

#Cx: cubo tomba para tras
  fu=c[up][:]    #face up    = white
  fd=c[down][:]  #face down  = yellow
  ff=c[front][:] #face front = red
  fb=c[back][:]  #face back  = orange
  fr=c[right][:] #face right = blue - nao muda
  fl=c[left][:]  #face left  = green 
  #up
  c[up][0]=fb[8]
  c[up][3]=fb[5]
  c[up][6]=fb[2]
  #down
  c[down][0]=ff[0]
  c[down][3]=ff[3]
  c[down][6]=ff[6]
  #front
  c[front][0]=fu[0]
  c[front][3]=fu[3]
  c[front][6]=fu[6]
  #back
  c[back][2]=fd[6]
  c[back][5]=fd[3]
  c[back][8]=fd[0]
  #right
  c[right][2]=fd[8]
  c[right][5]=fd[7]
  c[right][8]=fd[6]
  #left
  c[left][0]=fl[6]
  c[left][1]=fl[3]
  c[left][2]=fl[0]
  c[left][3]=fl[7]
  c[left][4]=fl[4]
  c[left][5]=fl[1]
  c[left][6]=fl[8]
  c[left][7]=fl[5]
  c[left][8]=fl[2]

#Cy: cubo gira na mesa

#Cz: cubo gira tomba para direita

acao=[u, ui, d, di, f, fi, b, bi, r, ri, l, li, u2, d2, f2, b2, r2, l2]
nacao=['U', 'Ui', 'D', 'Di', 'F', 'Fi', 'B', 'Bi', 'R', 'Ri', 'L', 'Li', 'U2', 'D2', 'F2', 'B2', 'R2', 'L2']
MAXACAO=len(acao)

def embaralha(c, n):
  """
    Dado um cubo c e a quantidade de movimentos n, faz n movimentos aleatorios em c
  """
  print("Embaralhado com: ", end="")
  while(n!=0):
    s=randint(0, MAXACAO-1)
    acao[s](c)
    print(nacao[s], ' ', end="")
    n=n-1
  print()

def soluciona(c, acoes):
  for s in acoes:
    acao[s](c)

def buscarec(o, c, nmax, natual, acoes):
  """
    Funcao recursiva para buscar os nos. Esta e a funcao mais importante do problema.
    - Recebe o cubo objeto o, o cubo a ser analisado c, o nivel maximo a se adentrar,
    o nivel atual que esta olhando, e a lista de acoes para a solucao do problema
    - Retorna o numero de nos procurados, e atualiza a lista de acoes para o problema
  """
  global achou, nos
  natual = natual + 1
  if natual > nmax:
    return 0
  for a in range(0, MAXACAO):
    t=deepcopy(c)
    acao[a](t)
    nos = nos + 1
    if t == o: #achou
      achou = 1
    if achou: #achou neste nivel
      acoes.append(a)
      break
    else:
      q = deepcopy(t)
      buscarec(o, q, nmax, natual, acoes) #Busca recursiva neste no da arvore. Retorna na linha de baixo.
      if achou: #achou no nivel de baixo
        acoes.append(a)
        break
  return nos

def buscar(o, c, nmax, acoes):
  """
    Função que marca o tempo de trabalho da função buscarec()
    retorna tempo, nos
  """
  tini=time()
  global achou, nos
  achou = nos = 0
  t=deepcopy(c)
  nos = buscarec(o, t, nmax, 0, acoes)
  acoes.reverse()
  return time()-tini, nos

def busca(o, c, nmax, acoes):
  """
    Função de interface com o programa principal main().
    Recebe o cubo objetivo o, o cubo embaralhado c, o nível máximo a procurar, e a lista de ações da solução vazia.
    Retorna o tempo total, o número de nodos total e as ações para a solução
    Chama a função buscar, com diferentes n
  """
  ttotal = ntotal = 0
  for n in range(1, nmax+1):
    print('Iniciando busca em %2d' % n, end="")
    if n==1:
      print(' nivel. ', end='')
    else:
      print(' niveis.', end='')
    tempo, nodos = buscar(o, c, n, acoes)
    ttotal += tempo
    ntotal += nodos
    print(' Tempo: %10.3f' % tempo, 's', 'Nodos: %10d' % nodos, end='')
    if acoes!=[]:
      print(' Solucao!')
      break
    else:
      print(' Sem solucao.')
  return ttotal, ntotal


def main():
  nivel = 2
  if len(sys.argv) == 1:
    print('Embaralhando com nivel 2.')
    print('Voce pode dizer o nivel chamando o programa rubikeco.py <n>.')
  else:
    nivel = int(sys.argv[1])
    print('Embaralhando com nivel %d.' % nivel)
  if nivel>8:
    nivel = 2
    print('Nivel maximo atual 8. Embaralhando com nivel 2.')

  rubik = [['w','w','w','w','w','w','w','w','w'],
        ['y','y','y','y','y','y','y','y','y'],
        ['r','r','r','r','r','r','r','r','r'],
        ['o','o','o','o','o','o','o','o','o'],
        ['b','b','b','b','b','b','b','b','b'],
        ['g','g','g','g','g','g','g','g','g']]
  #obj = copy.deepcopy(teste)
  # U  B  Li  B  L
  #print('Aplicando rotacao u(teste)...')
  #u(obj)
  #imprime(obj)
  #obj = copy.deepcopy(teste)
  #print('Aplicando rotacao ui(teste)...')
  #ui(obj)
  #imprime(obj)
  #obj = copy.deepcopy(teste)
  #print('Aplicando rotacao d(teste)...')
  #d(obj)
  #imprime(obj)
  #obj = copy.deepcopy(teste)
  #print('Aplicando rotacao f(teste)...')
  #f(obj)
  #imprime(obj)
  #obj = copy.deepcopy(teste)
  #print('Aplicando rotacao b(teste)...')
  #b(obj)
  #imprime(obj)
  #obj = copy.deepcopy(teste)
  #print('Aplicando rotacao r(teste)...')
  #r(obj)
  #imprime(obj)
  #obj = copy.deepcopy(teste)
  #print('Aplicando rotacao l(teste)...')
  #l(obj)
  #imprime(obj)

  obj = deepcopy(rubik)
  print('Antes de embaralhar:')
  imprime(obj)
  embaralha(rubik, nivel)
  print('Depois de embaralhado:')
  imprime(rubik)
  #buscar solucao
  print('Calculando solucao...')
  print('Aplicando rotacao UPi anti-horario ui(cubo)...')
  acoes=[]
  tempo, nodos, acoes = buscar(obj, rubik, 8, acoes)
  
  print('Tempo total: %10.3f' % tempo, 's', ' Nodos: ', nodos, ' Nodos/s: %.3f' % (nodos/tempo))
  print('Solucao:')
  for i in acoes:
    print(nacao[i], ' ', end="")
  print()

  soluciona(rubik, acoes)
  print('Depois de solucionado:')
  imprime(rubik)

if __name__ == "__main__":
  main()

