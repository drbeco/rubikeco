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
rubik = [['0o','1o','2o','3o','4o','5o','6o','7o','8o'],
         ['0g','1g','2g','3g','4g','5g','6g','7g','8g'],
         ['0w','1w','2w','3w','4w','5w','6w','7w','8w'],
         ['0b','1b','2b','3b','4b','5b','6b','7b','8b'],
         ['0y','1y','2y','3y','4y','5y','6y','7y','8y'],
         ['0r','1r','2r','3r','4r','5r','6r','7r','8r']]

def u(c): #rotacao up horario
    fu=c[up][:]    #face up    = white
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
    fu=c[up][:]    #face up    = white
    ff=c[front][:] #face front = red
    fb=c[back][:]  #face back  = orange
    fr=c[right][:] #face right = blue
    fl=c[left][:]  #face left  = green
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
    #down
    #front
    c[front][0]=fl[2]
    c[front][1]=fl[5]
    c[front][2]=fl[8]
    #back
    c[back][6]=fr[0]
    c[back][7]=fr[3]
    c[back][8]=fr[6]
    #right
    c[right][0]=ff[2]
    c[right][3]=ff[1]
    c[right][6]=ff[0]
    #left
    c[left][2]=fb[8]
    c[left][5]=fb[7]
    c[left][8]=fb[6]

def d(c): #rotacao down horario
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
    fd=c[down][:]  #face down  = yellow
    ff=c[front][:] #face front = red
    fb=c[back][:]  #face back  = orange
    fr=c[right][:] #face right = blue
    fl=c[left][:]  #face left  = green
    #up
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
    c[front][6]=fr[8]
    c[front][7]=fr[5]
    c[front][8]=fr[2]
    #back
    c[back][0]=fl[6]
    c[back][1]=fl[3]
    c[back][2]=fl[0]
    #right
    c[right][2]=fb[0]
    c[right][5]=fb[1]
    c[right][8]=fb[2]
    #left
    c[left][0]=ff[6]
    c[left][3]=ff[7]
    c[left][6]=ff[8]

def f(c): #rotacao front horario
    fu=c[up][:] #up = white
    fd=c[down][:] #down = yellow
    ff=c[front][:] #front = red
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
    fu=c[up][:]    #face up    = white
    fd=c[down][:]  #face down  = yellow
    ff=c[front][:] #face front = red
    fr=c[right][:] #face right = blue
    fl=c[left][:]  #face left  = green
    #up
    c[up][6]=fr[6]
    c[up][7]=fr[7]
    c[up][8]=fr[8]
    #down
    c[down][6]=fl[6]
    c[down][7]=fl[7]
    c[down][8]=fl[8]
    #front
    c[front][0]=ff[2]
    c[front][1]=ff[5]
    c[front][2]=ff[8]
    c[front][3]=ff[1]
    c[front][4]=ff[4]
    c[front][5]=ff[7]
    c[front][6]=ff[0]
    c[front][7]=ff[3]
    c[front][8]=ff[6]
    #back
    #right
    c[right][6]=fd[6]
    c[right][7]=fd[7]
    c[right][8]=fd[8]
    #left
    c[left][6]=fu[6]
    c[left][7]=fu[7]
    c[left][8]=fu[8]

def b(c): #rotacao back horario
    fu=c[up][:] #up = white
    fd=c[down][:] #down = yellow
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
    fu=c[up][:]    #face up    = white
    fd=c[down][:]  #face down  = yellow
    fb=c[back][:]  #face back  = orange
    fr=c[right][:] #face right = blue
    fl=c[left][:]  #face left  = green
    #up
    c[up][0]=fl[0]
    c[up][1]=fl[1]
    c[up][2]=fl[2]
    #down
    c[down][0]=fr[0]
    c[down][1]=fr[1]
    c[down][2]=fr[2]
    #front
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
    c[right][0]=fu[0]
    c[right][1]=fu[1]
    c[right][2]=fu[2]
    #left
    c[left][0]=fd[0]
    c[left][1]=fd[1]
    c[left][2]=fd[2]

def r(c): #rotacao right horario
    fu=c[up][:]    #face up    = white
    fd=c[down][:]  #face down  = yellow
    ff=c[front][:] #face front = red
    fb=c[back][:]  #face back  = orange
    fr=c[right][:] #face right = blue
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
    fu=c[up][:]    #face up    = white
    fd=c[down][:]  #face down  = yellow
    ff=c[front][:] #face front = red
    fb=c[back][:]  #face back  = orange
    fr=c[right][:] #face right = blue
    #up
    c[up][2]=fb[2]
    c[up][5]=fb[5]
    c[up][8]=fb[8]
    #down
    c[down][0]=ff[8]
    c[down][3]=ff[5]
    c[down][6]=ff[2]
    #front
    c[front][2]=fu[2]
    c[front][5]=fu[5]
    c[front][8]=fu[8]
    #back
    c[back][2]=fd[6]
    c[back][5]=fd[3]
    c[back][8]=fd[0]
    #right
    c[right][0]=fr[2]
    c[right][1]=fr[5]
    c[right][2]=fr[8]
    c[right][3]=fr[1]
    c[right][4]=fr[4]
    c[right][5]=fr[7]
    c[right][6]=fr[0]
    c[right][7]=fr[3]
    c[right][8]=fr[6]
    #left

def l(c): #rotacao left horario
    fu=c[up][:]    #face up    = white
    fd=c[down][:]  #face down  = yellow
    ff=c[front][:] #face front = red
    fb=c[back][:]  #face back  = orange
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
    fu=c[up][:]    #face up    = white
    fd=c[down][:]  #face down  = yellow
    ff=c[front][:] #face front = red
    fb=c[back][:]  #face back  = orange
    fl=c[left][:]  #face left  = green
    #up
    c[up][0]=ff[0]
    c[up][3]=ff[3]
    c[up][6]=ff[6]
    #down
    c[down][2]=fb[6]
    c[down][5]=fb[3]
    c[down][8]=fb[0]
    #front
    c[front][0]=fd[8]
    c[front][3]=fd[5]
    c[front][6]=fd[2]
    #back
    c[back][0]=fu[0]
    c[back][3]=fu[3]
    c[back][6]=fu[6]
    #right
    #left
    c[left][0]=fl[2]
    c[left][1]=fl[5]
    c[left][2]=fl[8]
    c[left][3]=fl[1]
    c[left][4]=fl[4]
    c[left][5]=fl[7]
    c[left][6]=fl[0]
    c[left][7]=fl[3]
    c[left][8]=fl[6]

#rotacoes duplas: u2, d2, f2, b2, r2, l2, mx2, my2, mz2, cx2, cy2, cz2

def u2(c): #rotacao dupla de cima
    fu=c[up][:]    #face up    = white
    ff=c[front][:] #face front = red
    fb=c[back][:]  #face back  = orange
    fr=c[right][:] #face right = blue
    fl=c[left][:]  #face left  = green
    #up
    c[up][0]=fu[8]
    c[up][1]=fu[7]
    c[up][2]=fu[6]
    c[up][3]=fu[5]
    c[up][4]=fu[4]
    c[up][5]=fu[3]
    c[up][6]=fu[2]
    c[up][7]=fu[1]
    c[up][8]=fu[0]
    #down
    #front
    c[front][0]=fb[8]
    c[front][1]=fb[7]
    c[front][2]=fb[6]
    #back
    c[back][6]=ff[2]
    c[back][7]=ff[1]
    c[back][8]=ff[0]
    #right
    c[right][0]=fl[8]
    c[right][3]=fl[5]
    c[right][6]=fl[2]
    #left
    c[left][2]=fr[6]
    c[left][5]=fr[3]
    c[left][8]=fr[0]

def d2(c): #rotacao dupla de baixo
    fd=c[down][:]  #face down  = yellow
    ff=c[front][:] #face front = red
    fb=c[back][:]  #face back  = orange
    fr=c[right][:] #face right = blue
    fl=c[left][:]  #face left  = green
    #up
    #down
    c[down][0]=fd[8]
    c[down][1]=fd[7]
    c[down][2]=fd[6]
    c[down][3]=fd[5]
    c[down][4]=fd[4]
    c[down][5]=fd[3]
    c[down][6]=fd[2]
    c[down][7]=fd[1]
    c[down][8]=fd[0]
    #front
    c[front][6]=fb[2]
    c[front][7]=fb[1]
    c[front][8]=fb[0]
    #back
    c[back][0]=ff[8]
    c[back][1]=ff[7]
    c[back][2]=ff[6]
    #right
    c[right][2]=fl[6]
    c[right][5]=fl[3]
    c[right][8]=fl[0]
    #left
    c[left][0]=fr[8]
    c[left][3]=fr[5]
    c[left][6]=fr[2]

def f2(c): #rotacao dupla da frente
    fu=c[up][:]    #face up    = white
    fd=c[down][:]  #face down  = yellow
    ff=c[front][:] #face front = red
    fr=c[right][:] #face right = blue
    fl=c[left][:]  #face left  = green
    #up
    c[up][6]=fd[6]
    c[up][7]=fd[7]
    c[up][8]=fd[8]
    #down
    c[down][6]=fu[6]
    c[down][7]=fu[7]
    c[down][8]=fu[8]
    #front
    c[front][0]=ff[8]
    c[front][1]=ff[7]
    c[front][2]=ff[6]
    c[front][3]=ff[5]
    c[front][4]=ff[4]
    c[front][5]=ff[3]
    c[front][6]=ff[2]
    c[front][7]=ff[1]
    c[front][8]=ff[0]
    #back
    #right
    c[right][6]=fl[6]
    c[right][7]=fl[7]
    c[right][8]=fl[8]
    #left
    c[left][6]=fr[6]
    c[left][7]=fr[7]
    c[left][8]=fr[8]

def b2(c): #rotacao dupla de trás
    fu=c[up][:]    #face up    = white
    fd=c[down][:]  #face down  = yellow
    fb=c[back][:]  #face back  = orange
    fr=c[right][:] #face right = blue
    fl=c[left][:]  #face left  = green
    #up
    c[up][0]=fd[0]
    c[up][1]=fd[1]
    c[up][2]=fd[2]
    #down
    c[down][0]=fu[0]
    c[down][1]=fu[1]
    c[down][2]=fu[2]
    #front
    #back
    c[back][0]=fb[8]
    c[back][1]=fb[7]
    c[back][2]=fb[6]
    c[back][3]=fb[5]
    c[back][4]=fb[4]
    c[back][5]=fb[3]
    c[back][6]=fb[2]
    c[back][7]=fb[1]
    c[back][8]=fb[0]
    #right
    c[right][0]=fl[0]
    c[right][1]=fl[1]
    c[right][2]=fl[2]
    #left
    c[left][0]=fr[0]
    c[left][1]=fr[1]
    c[left][2]=fr[2]

def r2(c): #rotacao dupla da direita
    fu=c[up][:]    #face up    = white
    fd=c[down][:]  #face down  = yellow
    ff=c[front][:] #face front = red
    fb=c[back][:]  #face back  = orange
    fr=c[right][:] #face right = blue
    #up
    c[up][2]=fd[6]
    c[up][5]=fd[3]
    c[up][8]=fd[0]
    #down
    c[down][0]=fu[8]
    c[down][3]=fu[5]
    c[down][6]=fu[2]
    #front
    c[front][2]=fb[2]
    c[front][5]=fb[5]
    c[front][8]=fb[8]
    #back
    c[back][2]=ff[2]
    c[back][5]=ff[5]
    c[back][8]=ff[8]
    #right
    c[right][0]=fr[8]
    c[right][1]=fr[7]
    c[right][2]=fr[6]
    c[right][3]=fr[5]
    c[right][4]=fr[4]
    c[right][5]=fr[3]
    c[right][6]=fr[2]
    c[right][7]=fr[1]
    c[right][8]=fr[0]
    #left

def l2(c): #rotacao dupla da esquerda
    fu=c[up][:]    #face up    = white
    fd=c[down][:]  #face down  = yellow
    ff=c[front][:] #face front = red
    fb=c[back][:]  #face back  = orange
    fl=c[left][:]  #face left  = green
    #up
    c[up][0]=fd[8]
    c[up][3]=fd[5]
    c[up][6]=fd[2]
    #down
    c[down][2]=fu[6]
    c[down][5]=fu[3]
    c[down][8]=fu[0]
    #front
    c[front][0]=fb[0]
    c[front][3]=fb[3]
    c[front][6]=fb[6]
    #back
    c[back][0]=ff[0]
    c[back][3]=ff[3]
    c[back][6]=ff[6]
    #right
    #left
    c[left][0]=fl[8]
    c[left][1]=fl[7]
    c[left][2]=fl[6]
    c[left][3]=fl[5]
    c[left][4]=fl[4]
    c[left][5]=fl[3]
    c[left][6]=fl[2]
    c[left][7]=fl[1]
    c[left][8]=fl[0]

#rotacoes da camada do meio, notacao:
# m: rlixi; mi: ril
# e: udiyi; ei: uid
# s: fibz; si: fbi

def m(c): #rotacao da camada do meio, eixo x, horario (como l)
    fu=c[up][:]    #face up    = white
    fd=c[down][:]  #face down  = yellow
    ff=c[front][:] #face front = red
    fb=c[back][:]  #face back  = orange
    #up
    c[up][1]=fb[1]
    c[up][4]=fb[4]
    c[up][7]=fb[7]
    #down
    c[down][1]=ff[7]
    c[down][4]=ff[4]
    c[down][7]=ff[1]
    #front
    c[front][1]=fu[1]
    c[front][4]=fu[4]
    c[front][7]=fu[7]
    #back
    c[back][1]=fd[7]
    c[back][4]=fd[4]
    c[back][7]=fd[1]
    #right
    #left

def mi(c): #rotacao da camada do meio, eixo x, anti-horario (como l)
    ri(c)
    l(c)
    cx(c)

def e(c): #rotacao da camada do meio, eixo y, horario (como d)
    ff=c[front][:] #face front = red
    fb=c[back][:]  #face back  = orange
    fr=c[right][:] #face right = blue
    fl=c[left][:]  #face left  = green
    #up
    #down
    #front
    c[front][3]=fr[7]
    c[front][4]=fr[4]
    c[front][5]=fr[1]
    #back
    c[back][3]=fl[7]
    c[back][4]=fl[4]
    c[back][5]=fl[1]
    #right
    c[right][1]=fb[3]
    c[right][4]=fb[4]
    c[right][7]=fb[5]
    #left
    c[left][1]=ff[3]
    c[left][4]=ff[4]
    c[left][7]=ff[5]

def ei(c): #rotacao da camada do meio, eixo y, anti-horario (como d)
    ui(c)
    d(c)
    cy(c)

def s(c): #rotacao da camada do meio, eixo z, horario (como f)
    fu=c[up][:]    #face up    = white
    fd=c[down][:]  #face down  = yellow
    fr=c[right][:] #face right = blue
    fl=c[left][:]  #face left  = green
    #up
    c[up][3]=fl[3]
    c[up][4]=fl[4]
    c[up][5]=fl[5]
    #down
    c[down][3]=fr[3]
    c[down][4]=fr[4]
    c[down][5]=fr[5]
    #front
    #back
    #right
    c[right][3]=fu[3]
    c[right][4]=fu[4]
    c[right][5]=fu[5]
    #left
    c[left][3]=fd[3]
    c[left][4]=fd[4]
    c[left][5]=fd[5]

def si(c): #rotacao da camada do meio, eixo z, anti-horario (como f)
    f(c)
    bi(c)
    czi(c)

def m2(c): #rotacao dupla da camada do meio, eixo x
    m(c)
    m(c)

def e2(c): #rotacao dupla da camada do meio, eixo y
    e(c)
    e(c)

def s2(c): #rotacao dupla da camada do meio, eixo z
    s(c)
    s(c)

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

def cx2(c): #rotacao dupla do cubo inteiro, eixo x
    cx(c)
    cx(c)

def cy2(c): #rotacao dupla do cubo inteiro, eixo y
    cy(c)
    cy(c)

def cz2(c): #rotacao dupla do cubo inteiro, eixo z
    cz(c)
    cz(c)


acao=[u, ui, d, di, f, fi, b, bi, r, ri, l, li, u2, d2, f2, b2, r2, l2, 
      m, mi, e, ei, s, si, m2, e2, s2,
      cx, cxi, cy, cyi, cz, czi, cx2, cy2, cz2]
nacao=['U', 'Ui', 'D', 'Di', 'F', 'Fi', 'B', 'Bi', 'R', 'Ri', 'L', 'Li', 'U2', 'D2', 'F2', 'B2', 'R2', 'L2', 
       'M', 'Mi', 'E', 'Ei', 'S', 'Si', 'M2', 'E2', 'S2',
       'X', 'Xi', 'Y', 'Yi', 'Z', 'Zi', 'X2', 'Y2', 'Z2']

#26 acoes de face
#9 acoes de orientacao
facao=[u, ui, d, di, f, fi, b, bi, r, ri, l, li, m, mi, e, ei, s, si,
            u2, d2, f2, b2, r2, l2, m2, e2, s2]
fnacao=['U', 'Ui', 'D', 'Di', 'F', 'Fi', 'B', 'Bi', 'R', 'Ri', 'L', 'Li', 'M', 'Mi', 'E', 'Ei', 'S', 'Si',
             'U2', 'D2', 'F2', 'B2', 'R2', 'L2', 'M2', 'E2', 'S2']

racao=[cx, cxi, cy, cyi, cz, czi, cx2, cy2, cz2]
rnacao=['X', 'Xi', 'Y', 'Yi', 'Z', 'Zi', 'X2', 'Y2', 'Z2']

#tchange={'white_up':'cube', 'white_cross':'face', 'white_corners':'face', 'yellow_up':'cube', 'yellow_cross':'face', 'solve':'face'}

MIN_ACAO=0
MAX_ACAO=len(acao)
BASIC_MIN_ACAO=0
BASIC_MAX_ACAO=18
FACE_MIN_ACAO=0
FACE_MAX_ACAO=27 #len(facao)
CUBE_MIN_ACAO=27
CUBE_MAX_ACAO=36 #len(oacao)

act={'min':MIN_ACAO, 'max':MAX_ACAO}

def typeaction(t):
    """
        Define o tipo de acoes validas para uso
    """
    global act
    if t == 'cube': # apenas roda o cubo por inteiro
        act={'min':CUBE_MIN_ACAO, 'max':CUBE_MAX_ACAO}
        return
    if t == 'basic': # move somente as faces externas
        act={'min':BASIC_MIN_ACAO, 'max':BASIC_MAX_ACAO}
        return
    if t == 'face': # faces externas e faces do meio
        act={'min':FACE_MIN_ACAO, 'max':FACE_MAX_ACAO}
        return
    #if t == 'all': # todas faces e cubo inteiro
    act={'min':MIN_ACAO, 'max':MAX_ACAO}

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

def imprimeacoes(acoes):
    """
        Imprime as siglas da solucao encontrada em acoes
    """
    for i in acoes:
        print(nacao[i], ' ', end="")
    print()

def embaralha(cub, lvl):
    """
        Dado um cubo c e a quantidade de movimentos n, faz n movimentos aleatorios em c
    """
    print("Embaralhado com: ", end="")
    embacoes=[]
    while(lvl!=0):
        sorte=randint(act['min'], act['max']-1)
        embacoes+=[sorte]
        acao[sorte](cub)
        print(nacao[sorte], ' ', end="")
        lvl=lvl-1
    print()
    return embacoes

def soluciona(cub, acoes):
    for i in acoes:
        acao[i](cub)

def buscarec(obj, cub, nmax, natual, acoes):
    """
        Funcao recursiva para buscar os nos. Esta e a funcao mais importante do problema.
        - Recebe o objetivo obj, o cubo a ser analisado c, o nivel maximo a se adentrar,
        o nivel atual que esta olhando, e a lista de acoes para a solucao do problema
        - Retorna o numero de nos procurados, e atualiza a lista de acoes para o problema
    """
    global achou, nos
    natual = natual + 1
    if natual > nmax or objetivo(cub, obj): #nivel estourou ou ja achou
        return 0
    for a in range(act['min'], act['max']):
        t=deepcopy(cub)
        acao[a](t)
        nos = nos + 1
        if objetivo(t, obj): #cumpriu o objetivo obj?
            achou = 1
        if achou: #achou neste nivel
            acoes.append(a)
            break
        else:
            q = deepcopy(t)
            buscarec(obj, q, nmax, natual, acoes) #Busca recursiva neste no da arvore. Retorna na linha de baixo.
            if achou: #achou no nivel de baixo
                acoes.append(a)
                break
    return nos

def buscar(obj, cub, nmax, acoes):
    """
        Função que marca o tempo de trabalho da função buscarec()
        retorna tempo, nos
    """
    tini=time()
    global achou, nos
    achou = nos = 0
    t=deepcopy(cub)
    nos = buscarec(obj, t, nmax, 0, acoes)
    acoes.reverse()
    return time()-tini, nos

def busca(obj, cub, nmax, acoes):
    """
        Função de interface com o programa principal main().
        Recebe o objetivo obj, o cubo embaralhado cub, o nível máximo a procurar, e a lista de ações da solução vazia.
        Retorna o tempo total, o número de nodos total e as ações para a solução
        Chama a função buscar, com diferentes n
    """
    ttotal = ntotal = 0
    if objetivo(cub, obj): #cumpriu o objetivo obj?
        print(' Tempo: %10.3f' % 0.0, 's', 'Nodos: %10d' % 0, 'Solucao!')
        return 0.0001, ntotal

    for n in range(1, nmax+1):
        print('Iniciando busca em %2d' % n, end="")
        if n==1:
            print(' nivel. ', end='')
        else:
            print(' niveis.', end='')
        sys.stdout.flush()
        tempo, nodos = buscar(obj, cub, n, acoes)
        ttotal += tempo
        ntotal += nodos
        print(' Tempo: %10.3f' % tempo, 's', 'Nodos: %10d' % nodos, end='')
        if acoes!=[]:
            print(' Solucao!')
            break
        else:
            print(' Sem solucao.')
    return ttotal, ntotal

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
# novos obj:
#    orientar o cubo todo com branco acima: white_up
#    orientar o cubo todo com amarelo acima: yellow_up
#    fazer cruz branca: white_cross
#    subir os cantos brancos: white_corners
#    fazer cruz amarela: yellow_cross
#    resolver todo o cubo: solve
    
#rubik = [['0o','1o','2o','3o','4o','5o','6o','7o','8o'],
#        ['0g','1g','2g','3g','4g','5g','6g','7g','8g'],
#        ['0w','1w','2w','3w','4w','5w','6w','7w','8w'],
#        ['0b','1b','2b','3b','4b','5b','6b','7b','8b'],
#        ['0y','1y','2y','3y','4y','5y','6y','7y','8y'],
#        ['0r','1r','2r','3r','4r','5r','6r','7r','8r']]

#back=0; left=1; up=2; right=3; down=4; front=5; 
def objetivo(t, obj):
    """
        Funcao que retorna verdadeiro/falso se o objetivo corrente foi alcancado
    """
    if obj == 'white_up':
        if t[up][4] == '4w' and t[front][4] == '4r':
            return True
        else:
            return False

    if obj == 'white_cross':
        if objetivo(t, 'white_up') \
        and t[up][1] == '1w' and t[up][3] == '3w' and t[up][4] == '4w' and t[up][5] == '5w' and t[up][7] == '7w':
            return True
        else:
            return False

    if obj == 'white_corners':
        if objetivo(t, 'white_cross') \
        and t[up][0] == '0w' and t[up][2] == '2w' and t[up][6] == '6w' and t[up][8] == '8w':
            return True
        else:
            return False

    if obj == 'yellow_up':
        if t[up][4] == '4y' and t[front][4] == '4o':
            return True
        else:
            return False

    if obj == 'solve':
        if t == rubik:
            return True
        else:
            return False
    return False #objective not found


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

    #  rubik = [['0o','1o','2o','3o','4o','5o','6o','7o','8o'],
    #        ['0g','1g','2g','3g','4g','5g','6g','7g','8g'],
    #        ['0w','1w','2w','3w','4w','5w','6w','7w','8w'],
    #        ['0b','1b','2b','3b','4b','5b','6b','7b','8b'],
    #        ['0y','1y','2y','3y','4y','5y','6y','7y','8y'],
    #        ['0r','1r','2r','3r','4r','5r','6r','7r','8r']]
    #cubo = copy.deepcopy(rubik)
    # U  B  Li  B  L
    #print('Aplicando rotacao u(cubo)...')
    #u(cubo)
    #imprime(cubo)
    #cubo = copy.deepcopy(rubik)
    #print('Aplicando rotacao ui(cubo)...')
    #ui(cubo)
    #imprime(cubo)
    #cubo = copy.deepcopy(rubik)
    #print('Aplicando rotacao d(cubo)...')
    #d(cubo)
    #imprime(cubo)
    #cubo = copy.deepcopy(rubik)
    #print('Aplicando rotacao f(cubo)...')
    #f(cubo)
    #imprime(cubo)
    #cubo = copy.deepcopy(rubik)
    #print('Aplicando rotacao b(cubo)...')
    #b(cubo)
    #imprime(cubo)
    #cubo = copy.deepcopy(rubik)
    #print('Aplicando rotacao r(cubo)...')
    #r(cubo)
    #imprime(cubo)
    #cubo = copy.deepcopy(rubik)
    #print('Aplicando rotacao l(cubo)...')
    #l(cubo)
    #imprime(cubo)

    print('Antes de embaralhar:')
    imprime(rubik)

    emb = deepcopy(rubik)
    #cxi(emb)
    #ei(emb)

    #Mi  Cz2  Li  U2
    #mi(emb)
    #cz2(emb)
    #li(emb)
    #u2(emb)

    # Test superflip
    # U R2 F B R B2 R U2 L B2 R
    # Ui Di R2 F Ri L B2 U2 F2

    # u(emb)
    # r2(emb)
    # f(emb)
    # b(emb)
    # r(emb)
    # b2(emb)
    # r(emb)
    # u2(emb)
    # l(emb)
    # b2(emb)
    # r(emb)
    # ui(emb)
    # di(emb)
    # r2(emb)
    # f(emb)
    # ri(emb)
    # l(emb)
    # b2(emb)
    # u2(emb)
    # f2(emb)

    # Test superflip XY2
    # B L2 D U L U2 L B2 R U2 L
    # Bi Fi L2 D Li R U2 B2 D2
    
    b(emb)
    l2(emb)
    d(emb)
    u(emb)
    l(emb)
    u2(emb)
    l(emb)
    b2(emb)
    r(emb)
    u2(emb)
    l(emb)
    bi(emb)
    fi(emb)
    l2(emb)
    d(emb)
    li(emb)
    r(emb)
    u2(emb)
    b2(emb)
    d2(emb)
   
    #embacoes=embaralha(emb, nivel)
    print('Depois de embaralhado:')
    imprime(emb)
    print('Embaralhado com:')
    #print('Xi, Ei')
    print('#Mi  Z2  Li  U2')
    print('# U R2 F B R B2 R U2 L B2 R Ui Di R2 F Ri L B2 U2 F2')
    #imprimeacoes(embacoes)


    #R  Cx  Cxi  Cz2
    #print('d')
    #d(emb)
    #imprime(emb)

    #print('u')
    #u(emb)
    #imprime(emb)

    #print('b')
    #b(emb)
    #imprime(emb)

    #print('cx')
    #cx(emb)
    #imprime(emb)

    #print('cy')
    #cy(emb)
    #imprime(emb)

    #print('cz')
    #cz(emb)
    #imprime(emb)

    #print('cxi')
    #cxi(emb)
    #imprime(emb)

    #cz2(emb)
    #imprime(emb)
    #emb = deepcopy(rubik)
    #mx(emb)
    #print('mx')
    #imprime(emb)
    #emb = deepcopy(rubik)
    #mxi(emb)
    #print('mxi')
    #imprime(emb)
    #emb = deepcopy(rubik)
    #my(emb)
    #print('my')
    #imprime(emb)
    #emb = deepcopy(rubik)
    #myi(emb)
    #print('myi')
    #imprime(emb)
    #emb = deepcopy(rubik)
    #mz(emb)
    #print('mz')
    #imprime(emb)
    #emb = deepcopy(rubik)
    #mzi(emb)
    #print('mzi')
    #imprime(emb)


#rodar cubo todo
#       'Cx', 'Cxi', 'Cy', 'Cyi', 'Cz', 'Czi',

    #emb = deepcopy(rubik)
    #cx(emb)
    #print('cx')
    #imprime(emb)
    #emb = deepcopy(rubik)
    #cxi(emb)
    #print('cxi')
    #imprime(emb)
    #emb = deepcopy(rubik)
    #cy(emb)
    #print('cy')
    #imprime(emb)
    #emb = deepcopy(rubik)
    #cyi(emb)
    #print('cyi')
    #imprime(emb)
    #emb = deepcopy(rubik)
    #cz(emb)
    #print('cz')
    #imprime(emb)
    #emb = deepcopy(rubik)
    #czi(emb)
    #print('czi')
    #imprime(emb)
    #emb = deepcopy(rubik)

    #buscar solucao
    print('Calculando solucao...')
    print('Method: Friedrich Beginer')
    tacoes=[]; ttempo=0; tnodos=0;

    fs=1
    acoes=[]
    print('\nFase %d: orientar cubo com face branca para cima e vermelha para frente' % fs)
    typeaction('cube')
    tempo, nodos = busca('white_up', emb, 8, acoes)
    ttempo += tempo; tnodos += nodos;
    soluciona(emb, acoes)  
    imprime(emb)
    print('Tempo total: %10.3f' % ttempo, 's', ' Nodos: ', tnodos, ' Nodos/s: %.3f' % (tnodos/ttempo))
    print('Solucao:')
    imprimeacoes(acoes)
    tacoes += acoes

    fs=fs+1
    acoes=[]
    print('\nFase %d: fazer cruz branca' % fs)
    typeaction('face')
    tempo, nodos = busca('white_cross', emb, 8, acoes)
    ttempo += tempo; tnodos += nodos;
    soluciona(emb, acoes)  
    imprime(emb)
    print('Tempo total: %10.3f' % ttempo, 's', ' Nodos: ', tnodos, ' Nodos/s: %.3f' % (tnodos/ttempo))
    print('Solucao:')
    imprimeacoes(acoes)
    tacoes += acoes

    fs=fs+1
    acoes=[]
    print('\nFase %d: subir os cantos brancos' % fs)
    typeaction('basic')
    tempo, nodos = busca('white_corners', emb, 8, acoes)
    ttempo += tempo; tnodos += nodos;
    soluciona(emb, acoes)  
    imprime(emb)
    print('Tempo total: %10.3f' % ttempo, 's', ' Nodos: ', tnodos, ' Nodos/s: %.3f' % (tnodos/ttempo))
    print('Solucao:')
    imprimeacoes(acoes)
    tacoes += acoes

    fs=fs+1
    acoes=[]
    print('\nFase %d: orientar o cubo com a face amarela para cima e laranja para frente' % fs)
    typeaction('cube')
    tempo, nodos = busca('yellow_up', emb, 8, acoes)
    ttempo += tempo; tnodos += nodos;
    soluciona(emb, acoes)  
    imprime(emb)
    print('Tempo total: %10.3f' % ttempo, 's', ' Nodos: ', tnodos, ' Nodos/s: %.3f' % (tnodos/ttempo))
    print('Solucao:')
    imprimeacoes(acoes)
    tacoes += acoes

    fs=fs+1
    acoes=[]
    print('\nFase %d: orientar o cubo com a face branca para cima e vermelha para frente' % fs)
    typeaction('cube')
    tempo, nodos = busca('white_up', emb, 8, acoes)
    ttempo += tempo; tnodos += nodos;
    soluciona(emb, acoes)  
    imprime(emb)
    print('Tempo total: %10.3f' % ttempo, 's', ' Nodos: ', tnodos, ' Nodos/s: %.3f' % (tnodos/ttempo))
    print('Solucao:')
    imprimeacoes(acoes)
    tacoes += acoes

    fs=fs+1
    acoes=[]
    print('\nFase %d: resolver todo o cubo' % fs)
    typeaction('face')
    tempo, nodos = busca('solve', emb, 8, acoes)
    ttempo += tempo; tnodos += nodos;
    soluciona(emb, acoes)  
    imprime(emb)
    print('Tempo total: %10.3f' % ttempo, 's', ' Nodos: ', tnodos, ' Nodos/s: %.3f' % (tnodos/ttempo))
    print('Solucao:')
    imprimeacoes(acoes)
    tacoes += acoes

    #soluciona(emb, acoes)  
    #print('Depois de solucionado:')
    #imprime(emb)

    print('Embaralhado com:')
    imprimeacoes(embacoes)
    print('Solucao total:')
    imprimeacoes(tacoes)

if __name__ == "__main__":
    main()


#/* ------------------------------------------------------------------------ */
#/* Python config for Vim modeline                                           */
#/* vi: set ai sta et ts=8 sts=4 sw=4 tw=79 wm=0 cc=+1 lbr fo=croq :         */
#/* Template by Dr. Beco <rcb at beco dot cc>        Version 20170724.161751 */

