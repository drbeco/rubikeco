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

#import copy
#import random
import threading
from copy import deepcopy
from random import randint
from time import time
import sys

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
  fu=c[up][:] #up = white
  fd=c[down][:] #down = yellow - nao muda
  ff=c[front][:] #front = red
  fb=c[back][:] #back = orange
  fr=c[right][:] #right = blue
  fl=c[left][:] #left = green
  #up
  c[up][0]=fu[2]
  c[up][1]=fu[5]
  c[up][2]=fu[8]
  c[up][3]=fu[1]
  c[up][4]=fu[4]
  c[up][5]=fu[7]
  c[up][6]=fu[0]
  c[up][7]=fu[3]
  c[up][8]=fu[6]
  #down   #nada muda
  #front
  c[front][0]=fl[0]
  c[front][1]=fl[1]
  c[front][2]=fl[2]
  #back
  c[back][0]=fr[0]
  c[back][1]=fr[1]
  c[back][2]=fr[2]
  #right
  c[right][0]=ff[0]
  c[right][1]=ff[1]
  c[right][2]=ff[2]
  #left
  c[left][0]=fb[0]
  c[left][1]=fb[1]
  c[left][2]=fb[2]

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
#  nc = [ff, fb, fd, fu, fr, fl]
#  c = deepcopy(nc)
  c[up]   =ff
  #print('teste')
  #print (fb)
  fb.reverse()
  c[down] =fb
  c[front]=fd
  fu.reverse()
  c[back] =fu
  c[right]=fr #bug
  c[left] =fl #bug
  #print('De dentro de cx:------------------')
  #imprime(c)

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
#  nc = [fu, fd, fr, fl, fb, ff]
#  c = deepcopy(nc)
  c[up]   =fu
  c[down] =fd
  c[front]=fr
  c[back] =fl
  c[right]=fb
  c[left] =ff

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
#  nc = [fl, fr, ff, fb, fu, fd]
#  c = deepcopy(nc)
  c[up]   =fl
  c[down] =fr
  c[front]=ff
  c[back] =fb
  c[right]=fu
  c[left] =fd

def czi(c): #rotacao do cubo inteiro, eixo z, anti-horario (cubo tomba para esquerda)
  cz(c)
  cz(c)
  cz(c)

#rotacoes da camada do meio:
# mx: ril; mxi: rli
# my: uid; myi: udi
# mz: fib; mzi: fbi

def mx(c): #rotacao da camada do meio, eixo x, horario
  ri(c)
  l(c)
  cx(c)

def mxi(c): #rotacao da camada do meio, eixo x, anti-horario
  r(c)
  li(c)
  cxi(c)

def my(c): #rotacao da camada do meio, eixo y, horario
  ui(c)
  d(c)
  cy(c)

def myi(c): #rotacao da camada do meio, eixo y, anti-horario
  u(c)
  di(c)
  cyi(c)

def mz(c): #rotacao da camada do meio, eixo z, horario
  fi(c)
  b(c)
  cz(c)

def mzi(c): #rotacao da camada do meio, eixo z, anti-horario
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

def mx2(c): #rotacao dupla da camada do meio, eixo x
  mx(c)
  mx(c)

def my2(c): #rotacao dupla da camada do meio, eixo y
  my(c)
  my(c)

def mz2(c): #rotacao dupla da camada do meio, eixo z
  mz(c)
  mz(c)

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

acao=[u, ui, d, di, f, fi, b, bi, r, ri, l, li]
nacao=['U', 'Ui', 'D', 'Di', 'F', 'Fi', 'B', 'Bi', 'R', 'Ri', 'L', 'Li']
#acao=[u, ui, d, di, f, fi, b, bi, r, ri, l, li,
#      mx, mxi, my, myi, mz, mzi,
#      cx, cxi, cy, cyi, cz, czi,
#      u2, d2, f2, b2, r2, l2, mx2, my2, mz2, cx2, cy2, cz2]
#nacao=['U', 'Ui', 'D', 'Di', 'F', 'Fi', 'B', 'Bi', 'R', 'Ri', 'L', 'Li',
#       'Mx', 'Mxi', 'My', 'Myi', 'Mz', 'Mzi',
#       'Cx', 'Cxi', 'Cy', 'Cyi', 'Cz', 'Czi',
#       'U2', 'D2', 'F2', 'B2', 'R2', 'L2', 'Mx2', 'My2', 'Mz2', 'Cx2', 'Cy2', 'Cz2']
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

class buscat(threading.Thread):
  """
    Funcao recursiva com threads para buscar os nos. Esta e a funcao mais importante do problema.
    - Recebe o cubo objeto o, o cubo a ser analisado c, o nivel maximo a se adentrar,
    o nivel atual que esta olhando, e a lista de acoes para a solucao do problema
    - Retorna o numero de nos procurados, e atualiza a lista de acoes para o problema
  """
  achou = 0
  nodos = 0
  acos = []
  def __init__ ( self, o, c, nmax):
    threading.Thread.__init__ ( self )
    self.o = o
    self.c = deepcopy(c)
    self.nmax = nmax
    #self.natual = natual
    #self.acoes = acoes
    self.nos = 1
    #self.name = nome

  def run(self):#, o, c, nmax, natual, acoes):
    """
      retorna numero de nodos pesquisados
    """
    #print(self.name)
    t = deepcopy(self.c)
    a = int(self.name)
    acao[a](t)
    if t == self.o:
      buscat.achou = self.name
      buscat.acos.append(a)
      buscat.acos = [a]
      return
    #print('em run, self.name:', self.name)
    self.buscatr(self.o, t, self.nmax, 1, self.name)
    if buscat.achou == self.name: #achou no nivel de baixo desta thread
      buscat.acos.append(a)
    return

  def buscatr(self, o, c, nmax, natual, npai):
    """
      recursiva. num. nodos calculados em self.nos
    """
    natual = natual + 1
    if natual > nmax:
      #print('if natual > nmax:')
      return
    if buscat.achou != 0:
      return
    if c == o:
      return
    for a in range(0, MAXACAO):
      t=deepcopy(c)
      acao[a](t)
      self.nos = self.nos + 1
      if t == o: #achou
        buscat.achou = npai
        buscat.acos.append(a)
        #if self.name=='Thread-1':
          #print('adicionou acos:', a, nacao[a], natual)
        break
      if buscat.achou != 0: #achou em alguma thread
        break
      else:
        q = deepcopy(t)
        self.buscatr(o, q, nmax, natual, npai)
        if buscat.achou == npai: #achou no nivel de baixo desta thread
          #if self.name=='Thread-1':
            #print('acos', buscat.acos)
          buscat.acos.append(a)
          #if self.name=='Thread-1':
            #print('->adicionou acos a', a, 'nacao:', nacao[a], 'natual', natual, 'achou', buscat.achou)
          break
    return

def buscar(o, c, nmax):
  """
    Função que marca o tempo de trabalho das threads 
    retorna tempo, nos
  """
  tini=time()
  tredis=[]
  n=[]
  for a in range(0, MAXACAO):
  #  t=deepcopy(c)
  #  acao[a](t)
  #  if t == o:
  #    buscat.achou = 1
  #    buscat.acos = [a]
  #    print('No threads started')
  #    ntotal = a+1;
  #    print ('Nodos calculados: ', ntotal)
  #    return time()-tini, ntotal, buscat.acos
    tredis.append(buscat(o, c, nmax))
    n.append(0)

  buscat.achou=0
  buscat.nodos=0
  buscat.acos=[]
  for i in range(0, MAXACAO):
    tredis[i].name = i
    #print(tredis[i].name)
    tredis[i].start() #n[i] = num nodos
  #print('All started')

  for i in range(0, MAXACAO):
    tredis[i].join()
    n[i]=tredis[i].nos
  #print('All joined')

  #print('achou: ', buscat.achou)
  #buscat.acos.append(int(buscat.achou))
#  try:
#  except KeyboardInterrupt:
#    exit()

  ntotal = 0;
  for i, j in enumerate(n):
    print ('Nodos calculados pela Thread-%02d: %2d ' % ((i+1), j), ' Movimento inicial: ', nacao[int(tredis[i].name)])
    ntotal = ntotal + j

  #for i,j in enumerate(t):
    #print(i, j)

  #nos = buscarec1(o, t, nmax, 0, acoes)
  buscat.acos.reverse()
  return time()-tini, ntotal, buscat.acos

def busca(o, c, nmax):
  """
    Função de interface com o programa principal main().
    Recebe o cubo objetivo o, o cubo embaralhado c, o nível máximo a procurar, e a lista de ações da solução vazia.
    Retorna o tempo total, o número de nodos total e as ações para a solução
    Chama a função buscar, com diferentes n
  """
  ttotal = ntotal = 0
  if o == c:
    print('Nivel: 0.\nResultado: Solucao!')
    return ttotal, ntotal, []
  else:
    print('Nivel: 0.\nResultado: Sem solucao.')

  for n in range(1, nmax+1):
    print('Nivel: %2d.' % n)
    tempo, nodos, acoes = buscar(o, c, n)
    ttotal += tempo
    ntotal += nodos
    print('Nivel: %2d.' % n, 'Tempo: %10.3f' % tempo, 's', 'Nodos: %10d' % nodos, 'Resultado: ', end='')
    if acoes!=[]:
      print(' Solucao!')
      break
    else:
      print(' Sem solucao.')
  return ttotal, ntotal, acoes


def main():
  #print('Entre com a posicao atual')
  print('Posicao inicial: cubo resolvido.')
  print('Topo     (U): branco     (w)')
  print('Baixo    (D): amarelo    (y)')
  print('Frente   (F): vermelho   (r)')
  print('Costas   (B): alaranjado (o)')
  print('Direita  (R): azul       (b)')
  print('Esquerda (L): verde      (g)')
  rubik = [['w','w','w','w','w','w','w','w','w'],
        ['y','y','y','y','y','y','y','y','y'],
        ['r','r','r','r','r','r','r','r','r'],
        ['o','o','o','o','o','o','o','o','o'],
        ['b','b','b','b','b','b','b','b','b'],
        ['g','g','g','g','g','g','g','g','g']]
  #rubik = [['0o','1o','2o','3o','4o','5o','6o','7o','8o'],
  #      ['0g','1g','2g','3g','4g','5g','6g','7g','8g'],
  #      ['0w','1w','2w','3w','4w','5w','6w','7w','8w'],
  #      ['0b','1b','2b','3b','4b','5b','6b','7b','8b'],
  #      ['0y','1y','2y','3y','4y','5y','6y','7y','8y'],
  #      ['0r','1r','2r','3r','4r','5r','6r','7r','8r']]

  obj = deepcopy(rubik)
  # U  B  Li  B  L
  #embaralha(rubik, 5)
  #u(rubik)
  #b(rubik)
  #li(rubik)
  #b(rubik)
  #l(rubik)
  #print('u, b, li, b, l')

  # Ri Di, R, D, Ri, Di, R
  ri(rubik)
  di(rubik)
  r(rubik)
  d(rubik)
  ri(rubik)
  di(rubik)
  r(rubik)
  print('Ri Di, R, D, Ri, Di, R')
  imprime(rubik)

  #buscar solucao
  print('Calculando solucao...')
  acoes=[]

  #tempo, nodos =  busca(obj, rubik, 8, acoes)

  #def __init__ ( self, o, c, nmax, natual, acoes):

  tempo, nodos, acoes = busca(obj, rubik, 6)

  #print(tempo, nodos, acoes)

  #exit()
  #tempo, nodos =  buscat.busca(obj, rubik, 6, acoes)

  print('Total de tempo: %10.3f' % tempo, 's', '   Total de nodos: ', nodos, end='')
  if tempo!=0:
    print('   Nodos/s: %.3f' % (nodos/tempo))
  else:
    print('   Nodos/s: n/a')
  print('Solucao:')
  if acoes == []:
    print('[]', end='')
  else:
    for i in acoes:
      print(nacao[i], ' ', end="")
  print()

if __name__ == "__main__":
  main()

