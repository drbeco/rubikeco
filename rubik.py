#!/usr/bin/python
# -*- coding: utf-8 -*-
# (C) Copyright 2010-2017 by Ruben Carlo Benante <rcb@beco.cc>

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
  print('Calculando solucao...')
  print('Aplicando rotacao UPi anti-horario ui(cubo)...')
  ui(ini)
  print('Cubo:')
  print(ini)

if __name__ == "__main__":
  main()
  
