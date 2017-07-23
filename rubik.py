#!/usr/bin/python
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

def ui(r): #rotacao up anti-horario
  fu=r[0][:] #up = white
  fd=r[1][:] #down = yellow - nao muda
  ff=r[2][:] #front = red
  fb=r[3][:] #back = orange
  fr=r[4][:] #right = green
  fl=r[5][:] #left = blue
  #up
  r[0][0]=fu[2]
  r[0][1]=fu[5]
  r[0][2]=fu[8]
  r[0][3]=fu[1]
  r[0][4]=fu[4]
  r[0][5]=fu[7]
  r[0][6]=fu[0]
  r[0][7]=fu[3]
  r[0][8]=fu[6]
  #down   #nada muda
  #front
  r[2][0]=fl[0]
  r[2][1]=fl[1]
  r[2][2]=fl[2]
  #back
  r[3][0]=fr[0]
  r[3][1]=fr[1]
  r[3][2]=fr[2]
  #right
  r[4][0]=ff[0]
  r[4][1]=ff[1]
  r[4][2]=ff[2]
  #left
  r[5][0]=fb[0]
  r[5][1]=fb[1]
  r[5][2]=fb[2]
  
def main():
  print('Entre com a posicao atual')
  obj =   [['w','w','w','w','w','w','w','w','w'],
	   ['y','y','y','y','y','y','y','y','y'],
	   ['r','r','r','r','r','r','r','r','r'],
           ['o','o','o','o','o','o','o','o','o'],  
	   ['g','g','g','g','g','g','g','g','g'],
	   ['b','b','b','b','b','b','b','b','b']]
  ini =   [['y','w','w','w','w','w','w','w','w'],
	   ['w','y','y','y','y','y','y','y','y'],
	   ['r','r','r','r','r','r','r','r','r'],
           ['o','o','o','o','o','o','o','o','o'],  
	   ['g','g','g','g','g','g','g','g','g'],
	   ['b','b','b','b','b','b','b','b','b']]

  rubik = [['w','w','w','w','w','w','w','w','w'],
        ['y','y','y','y','y','y','y','y','y'],
        ['r','r','r','r','r','r','r','r','r'],
        ['o','o','o','o','o','o','o','o','o'],
        ['b','b','b','b','b','b','b','b','b'],
        ['g','g','g','g','g','g','g','g','g']]
  obj = copy.deepcopy(teste)
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
  
  #buscar solucao
  print('Calculando solucao...')
  print('Aplicando rotacao UPi anti-horario ui(cubo)...')
  acoes=[]
  #tempo=0.0
  #tempo, nodos =  busca(obj, rubik, 8, acoes)
  
 # def __init__ ( self, o, c, nmax, natual, acoes):
  
  tempo, nodos, acoes = buscar(obj, rubik, 6, acoes)
  
  #print(tempo, nodos, acoes)
  
  #exit()
  #tempo, nodos =  buscat.busca(obj, rubik, 6, acoes)

  print('Tempo total: %10.3f' % tempo, 's', ' Nodos: ', nodos, ' Nodos/s: %.3f' % (nodos/tempo))
  print('Solucao:')
  for i in acoes:
    print(nacao[i], ' ', end="")
  print()

if __name__ == "__main__":
  main()
  
