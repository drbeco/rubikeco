#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright 2010-2017 Prof. Dr. Ruben Carlo Benante Version 1.2.20170724.014721
# Autor: Ruben Carlo Benante <rcb@beco.cc>
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
import sys

back=0; left=1; up=2; right=3; down=4; front=5; 
achou = 0; nos = 0;

def imprime(cubo):
  """
    Imprime o cubo 'desmontado'
  """
  print("             B")
  print("          ", end='')
  for p in range(9):
    if p%3==0 and p!=0:
      print()
      print("          ", end='')
    print(cubo[0][p], '', end='')
  print()
  print("   L         U         R         D")
  for p in range(3):
    for f in range(1,5):
      print(cubo[f][p*3+0], cubo[f][p*3+1], cubo[f][p*3+2], " ", end='')
    print()
  print("             F")
  print("          ", end='')
  for p in range(9):
    if p%3==0 and p!=0:
      print()
      print("          ", end='')
    print(cubo[5][p], '', end='')
  print()

def imprimefaces(cubo):
  """
    Imprime o cubo, cada face separadamente
  """
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
  c[front][0]=fr[6]
  c[front][1]=fr[3]
  c[front][2]=fr[0]
  #back
  c[back][6]=fl[8]
  c[back][7]=fl[5]
  c[back][8]=fl[2]
  #right
  c[right][0]=fb[6]
  c[right][3]=fb[7]
  c[right][6]=fb[8]
  #left
  c[left][2]=ff[0]
  c[left][5]=ff[1]
  c[left][8]=ff[2]

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
  c[front][6]=fl[0]
  c[front][7]=fl[3]
  c[front][8]=fl[6]
  #back
  c[back][0]=fr[2]
  c[back][1]=fr[5]
  c[back][2]=fr[8]
  #right
  c[right][2]=ff[8]
  c[right][5]=ff[7]
  c[right][8]=ff[6]
  #left
  c[left][0]=fb[2]
  c[left][3]=fb[1]
  c[left][6]=fb[0]

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
  c[up][6]=fl[6]
  c[up][7]=fl[7]
  c[up][8]=fl[8]
  #down
  c[down][6]=fr[6]
  c[down][7]=fr[7]
  c[down][8]=fr[8]
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
  c[right][6]=fu[6]
  c[right][7]=fu[7]
  c[right][8]=fu[8]
  #left
  c[left][6]=fd[6]
  c[left][7]=fd[7]
  c[left][8]=fd[8]

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
  c[up][0]=fr[0]
  c[up][1]=fr[1]
  c[up][2]=fr[2]
  #down 1
  c[down][0]=fl[0]
  c[down][1]=fl[1]
  c[down][2]=fl[2]
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
  c[right][0]=fd[0]
  c[right][1]=fd[1]
  c[right][2]=fd[2]
  #left 5
  c[left][0]=fu[0]
  c[left][1]=fu[1]
  c[left][2]=fu[2]

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
  c[down][0]=fb[8]
  c[down][3]=fb[5]
  c[down][6]=fb[2]
  #front
  c[front][2]=fd[6]
  c[front][5]=fd[3]
  c[front][8]=fd[0]
  #back
  c[back][2]=fu[2]
  c[back][5]=fu[5]
  c[back][8]=fu[8]
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
  c[up][0]=fb[0]
  c[up][3]=fb[3]
  c[up][6]=fb[6]
  #down
  c[down][2]=ff[6]
  c[down][5]=ff[3]
  c[down][8]=ff[0]
  #front
  c[front][0]=fu[0]
  c[front][3]=fu[3]
  c[front][6]=fu[6]
  #back
  c[back][0]=fd[8]
  c[back][3]=fd[5]
  c[back][6]=fd[2]
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

#Rotacionar o cubo inteiro
#Cx, Cxi, Cy, Cyi, Cz, Czi
#  rubik = [ U = ['w','w','w','w','w','w','w','w','w'],
#            D = ['y','y','y','y','y','y','y','y','y'],
#            F = ['r','r','r','r','r','r','r','r','r'],
#            B = ['o','o','o','o','o','o','o','o','o'],
#            R = ['b','b','b','b','b','b','b','b','b'],
#            L = ['g','g','g','g','g','g','g','g','g']]

#Cx: cubo tomba para tras
#Cy: cubo gira na mesa
#Cz: cubo gira tomba para direita

def cx(c): #rotacao do cubo inteiro, eixo x, horario (cubo tomba para trás)
  fu=c[up][:]    #face up    = white
  fd=c[down][:]  #face down  = yellow
  ff=c[front][:] #face front = red
  fb=c[back][:]  #face back  = orange
  fr=c[right][:] #face right = blue - nao muda
  fl=c[left][:]  #face left  = green
  #up
  c[up]=ff
  #down
  fb.reverse()
  c[down]=fb
  #front
  fd.reverse()
  c[front]=fd
  #back
  c[back]=fu
  #right (r)
  c[right][0]=fr[6]
  c[right][1]=fr[3]
  c[right][2]=fr[0]
  c[right][3]=fr[7]
  c[right][4]=fr[4]
  c[right][5]=fr[1]
  c[right][6]=fr[8]
  c[right][7]=fr[5]
  c[right][8]=fr[2]
  #left (li)
  c[left][0]=fl[2]
  c[left][1]=fl[5]
  c[left][2]=fl[8]
  c[left][3]=fl[1]
  c[left][4]=fl[4]
  c[left][5]=fl[7]
  c[left][6]=fl[0]
  c[left][7]=fl[3]
  c[left][8]=fl[6]

def cxi(c): #rotacao do cubo inteiro, eixo x, anti-horario (cubo tomba para frente)
  cx(c)
  cx(c)
  cx(c)

def cy(c): #rotacao do cubo inteiro, eixo y, horario (cubo gira na mesa)
  fu=c[up][:]    #face up    = white
  fd=c[down][:]  #face down  = yellow
  ff=c[front][:] #face front = red
  fb=c[back][:]  #face back  = orange
  fr=c[right][:] #face right = blue - nao muda
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
  #down
  c[down][0]=fd[2]
  c[down][1]=fd[5]
  c[down][2]=fd[8]
  c[down][3]=fd[1]
  c[down][4]=fd[4]
  c[down][5]=fd[7]
  c[down][6]=fd[0]
  c[down][7]=fd[3]
  c[down][8]=fd[6]
  #front
  c[front][0]=fr[6]
  c[front][1]=fr[3]
  c[front][2]=fr[0]
  c[front][3]=fr[7]
  c[front][4]=fr[4]
  c[front][5]=fr[1]
  c[front][6]=fr[8]
  c[front][7]=fr[5]
  c[front][8]=fr[2]
  #back
  c[back][0]=fl[6]
  c[back][1]=fl[3]
  c[back][2]=fl[0]
  c[back][3]=fl[7]
  c[back][4]=fl[4]
  c[back][5]=fl[1]
  c[back][6]=fl[8]
  c[back][7]=fl[5]
  c[back][8]=fl[2]
  #right
  c[right][0]=fb[6]
  c[right][1]=fb[3]
  c[right][2]=fb[0]
  c[right][3]=fb[7]
  c[right][4]=fb[4]
  c[right][5]=fb[1]
  c[right][6]=fb[8]
  c[right][7]=fb[5]
  c[right][8]=fb[2]
  #left
  c[left][0]=ff[6]
  c[left][1]=ff[3]
  c[left][2]=ff[0]
  c[left][3]=ff[7]
  c[left][4]=ff[4]
  c[left][5]=ff[1]
  c[left][6]=ff[8]
  c[left][7]=ff[5]
  c[left][8]=ff[2]

def cyi(c): #rotacao do cubo inteiro, eixo y, anti-horario (cubo gira na mesa)
  cy(c)
  cy(c)
  cy(c)

def cz(c): #rotacao do cubo inteiro, eixo z, horario (cubo tomba para direita)
  fu=c[up][:]    #face up    = white
  fd=c[down][:]  #face down  = yellow
  ff=c[front][:] #face front = red
  fb=c[back][:]  #face back  = orange
  fr=c[right][:] #face right = blue - nao muda
  fl=c[left][:]  #face left  = green
  #up
  c[up]=fl
  #down
  c[down]=fr
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
  #back
  c[back][0]=fb[2]
  c[back][1]=fb[5]
  c[back][2]=fb[8]
  c[back][3]=fb[1]
  c[back][4]=fb[4]
  c[back][5]=fb[7]
  c[back][6]=fb[0]
  c[back][7]=fb[3]
  c[back][8]=fb[6]
  #right
  c[right]=fu
  #left
  c[left]=fd

def czi(c): #rotacao do cubo inteiro, eixo z, anti-horario (cubo tomba para esquerda)
  cz(c)
  cz(c)
  cz(c)

#rotacoes da camada do meio, notacao:
# m: rli; mi: ril
# e: udi; ei: uid
# s: fib; si: fbi

def m(c): #rotacao da camada do meio, eixo x, horario (como l)
  r(c)
  li(c)
  cxi(c)

def mi(c): #rotacao da camada do meio, eixo x, anti-horario (como l)
  ri(c)
  l(c)
  cx(c)

def e(c): #rotacao da camada do meio, eixo y, horario (como d)
  u(c)
  di(c)
  cyi(c)

def ei(c): #rotacao da camada do meio, eixo y, anti-horario (como d)
  ui(c)
  d(c)
  cy(c)

def s(c): #rotacao da camada do meio, eixo z, horario (como f)
  fi(c)
  b(c)
  cz(c)

def si(c): #rotacao da camada do meio, eixo z, anti-horario (como f)
  f(c)
  bi(c)
  czi(c)

#rotacoes duplas: u2, d2, f2, b2, r2, l2, mx2, my2, mz2, cx2, cy2, cz2

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

def m2(c): #rotacao dupla da camada do meio, eixo x
  m(c)
  m(c)

def e2(c): #rotacao dupla da camada do meio, eixo y
  e(c)
  e(c)

def s2(c): #rotacao dupla da camada do meio, eixo z
  s(c)
  s(c)

def cx2(c): #rotacao dupla do cubo inteiro, eixo x
  cx(c)
  cx(c)

def cy2(c): #rotacao dupla do cubo inteiro, eixo y
  cy(c)
  cy(c)

def cz2(c): #rotacao dupla do cubo inteiro, eixo z
  cz(c)
  cz(c)

#Manobras
#S1:  #E2:   Ri U Fi Ui                      #cruz branca
#S2:  #E3:   Ri Di R D                       #cantos brancos
#S3:  #E41:  U R Ui Ri Ui Fi U F             #mover horario
#S4:  #E42:  Ui Li U L U F Ui Fi             #mover anti-horario
#S5:  #E511: F U R Ui Ri Fi                  #amarelo no centro, ou L
#S6:  #E512: F R U Ri Ui Fi                  #reta amarela
#S7:  #E521: R U Ri U R U U Ri               #subir os cantos amarelos
#S8:  #E522: Li Ui L Ui Li Ui Ui L           #subir os cantos amarelos espelhado
#S9:  #E61:  Ri F Ri B B R Fi Ri B B R R Ui  #corrigir os cantos amarelos
#S10: #E621: F F U L Ri F F Li R U F F       #rodar arestas horario
#S11: #E622: F F Ui L Ri F F Li R Ui F F     #rodar arestas anti-horario

# rotacao nos eixos
# x=r=li=mi
# y=u=di=ei
# z=f=bi=s

# Testes
# cubo pronto
# CFOP:
#   cruz branca (cor neutra)
#   face branca
#   2 camadas
#   topo amarelo
#   topo amarelo com cantos
# Roux
#   1 bloco 1x2x3
#   2 blocos 1x2x3
# Petrus
#   bloco 2x2x2
# X corner first
#   todas quinas

acao=[u, ui, d, di, f, fi, b, bi, r, ri, l, li,
      m, mi, e, ei, s, si,
      cx, cxi, cy, cyi, cz, czi,
      u2, d2, f2, b2, r2, l2, m2, e2, s2, cx2, cy2, cz2]
nacao=['U', 'Ui', 'D', 'Di', 'F', 'Fi', 'B', 'Bi', 'R', 'Ri', 'L', 'Li',
       'M', 'Mi', 'E', 'Ei', 'S', 'Si',
       'Cx', 'Cxi', 'Cy', 'Cyi', 'Cz', 'Czi',
       'U2', 'D2', 'F2', 'B2', 'R2', 'L2', 'M2', 'E2', 'S2', 'Cx2', 'Cy2', 'Cz2']
MAXACAO=len(acao)

def embaralha(c, n):
  """
    Dado um cubo c e a quantidade de movimentos n, faz n movimentos aleatorios em c
  """
  print("Embaralhado com: ", end="")
  embacoes=[]
  while(n!=0):
    s=randint(0, MAXACAO-1)
    embacoes+=[s]
    acao[s](c)
    print(nacao[s], ' ', end="")
    n=n-1
  print()
  return embacoes

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
  #print('Entre com a posicao atual')
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

  #rubik = [['w','w','w','w','w','w','w','w','w'],
  #      ['y','y','y','y','y','y','y','y','y'],
  #      ['r','r','r','r','r','r','r','r','r'],
  #      ['o','o','o','o','o','o','o','o','o'],
  #      ['b','b','b','b','b','b','b','b','b'],
  #      ['g','g','g','g','g','g','g','g','g']]
  #cubo = [['0w','1w','2w','3w','4w','5w','6w','7w','8w'],
        #['0y','1y','2y','3y','4y','5y','6y','7y','8y'],
        #['0r','1r','2r','3r','4r','5r','6r','7r','8r'],
        #['0o','1o','2o','3o','4o','5o','6o','7o','8o'],
        #['0b','1b','2b','3b','4b','5b','6b','7b','8b'],
        #['0g','1g','2g','3g','4g','5g','6g','7g','8g']]
  #obj = copy.deepcopy(cubo)
  # U  B  Li  B  L
  #print('Aplicando rotacao u(cubo)...')
  #back=0; left=1; up=2; right=3; down=4; front=5; 
  rubik = [['0o','1o','2o','3o','4o','5o','6o','7o','8o'],
        ['0g','1g','2g','3g','4g','5g','6g','7g','8g'],
        ['0w','1w','2w','3w','4w','5w','6w','7w','8w'],
        ['0b','1b','2b','3b','4b','5b','6b','7b','8b'],
        ['0y','1y','2y','3y','4y','5y','6y','7y','8y'],
        ['0r','1r','2r','3r','4r','5r','6r','7r','8r']]
  #u(obj)
  #imprime(obj)
  #obj = copy.deepcopy(cubo)
  #print('Aplicando rotacao ui(cubo)...')
  #ui(obj)
  #imprime(obj)
  #obj = copy.deepcopy(cubo)
  #print('Aplicando rotacao d(cubo)...')
  #d(obj)
  #imprime(obj)
  #obj = copy.deepcopy(cubo)
  #print('Aplicando rotacao f(cubo)...')
  #f(obj)
  #imprime(obj)
  #obj = copy.deepcopy(cubo)
  #print('Aplicando rotacao b(cubo)...')
  #b(obj)
  #imprime(obj)
  #obj = copy.deepcopy(cubo)
  #print('Aplicando rotacao r(cubo)...')
  #r(obj)
  #imprime(obj)
  #obj = copy.deepcopy(cubo)
  #print('Aplicando rotacao l(cubo)...')
  #l(obj)
  #imprime(obj)

  obj = deepcopy(rubik)
  print('Antes de embaralhar:')
  imprime(obj)
  embacoes=embaralha(rubik, nivel)
  print('Depois de embaralhado:')
  imprime(rubik)

  #R  Cx  Cxi  Cz2
  #print('d')
  #d(rubik)
  #imprime(rubik)

  #print('u')
  #u(rubik)
  #imprime(rubik)

  #print('b')
  #b(rubik)
  #imprime(rubik)

  #print('cx')
  #cx(rubik)
  #imprime(rubik)

  #print('cy')
  #cy(rubik)
  #imprime(rubik)

  #print('cz')
  #cz(rubik)
  #imprime(rubik)

  #print('cxi')
  #cxi(rubik)
  #imprime(rubik)

  #cz2(rubik)
  #imprime(rubik)
  #rubik = deepcopy(obj)
  #mx(rubik)
  #print('mx')
  #imprime(rubik)
  #rubik = deepcopy(obj)
  #mxi(rubik)
  #print('mxi')
  #imprime(rubik)
  #rubik = deepcopy(obj)
  #my(rubik)
  #print('my')
  #imprime(rubik)
  #rubik = deepcopy(obj)
  #myi(rubik)
  #print('myi')
  #imprime(rubik)
  #rubik = deepcopy(obj)
  #mz(rubik)
  #print('mz')
  #imprime(rubik)
  #rubik = deepcopy(obj)
  #mzi(rubik)
  #print('mzi')
  #imprime(rubik)


#rodar cubo todo
#       'Cx', 'Cxi', 'Cy', 'Cyi', 'Cz', 'Czi',

  #rubik = deepcopy(obj)
  #cx(rubik)
  #print('cx')
  #imprime(rubik)
  #rubik = deepcopy(obj)
  #cxi(rubik)
  #print('cxi')
  #imprime(rubik)
  #rubik = deepcopy(obj)
  #cy(rubik)
  #print('cy')
  #imprime(rubik)
  #rubik = deepcopy(obj)
  #cyi(rubik)
  #print('cyi')
  #imprime(rubik)
  #rubik = deepcopy(obj)
  #cz(rubik)
  #print('cz')
  #imprime(rubik)
  #rubik = deepcopy(obj)
  #czi(rubik)
  #print('czi')
  #imprime(rubik)
  #rubik = deepcopy(obj)


  #buscar solucao
  print('Calculando solucao...')
  acoes=[]
  #tempo, nodos = buscar(obj, rubik, 8, acoes)
  tempo, nodos = busca(obj, rubik, 8, acoes)

  print('Tempo total: %10.3f' % tempo, 's', ' Nodos: ', nodos, ' Nodos/s: %.3f' % (nodos/tempo))

  soluciona(rubik, acoes)  
  print('Depois de solucionado:')
  imprime(rubik)

  print('Embaralhado com:')
  for s in embacoes:
    print(nacao[s], ' ', end="")
  print()
  print('Solucao:')
  for i in acoes:
    print(nacao[i], ' ', end="")
  print()

if __name__ == "__main__":
  main()

