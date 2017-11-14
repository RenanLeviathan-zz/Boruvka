'''
Created on 13 de nov de 2017

@author: Israël & Renan
'''
from plot import *
global T
T=[]
grafo={"vertices":['0','1','2','3','4','5','6'],
       "arestas":[
         ('0','2',5),
         ('0','3',8),
         ('1','2',16),
         ('1','4',30),
         ('1','6',26),
         ('2','3',10),
         ('2','4',3),
         ('3','4',2),
         ('3','5',18),
         ('4','5',12),
         ('4','6',14),
         ('5','6',4)
         ]
  }
pos={
  '0':(50,100),
  '1':(200,50),
  '2':(100,50),
  '3':(100,150),
  '4':(150,100),
  '5':(200,150),
  '6':(250,100)
  }
grafo["arestas"].sort(key=lambda a:a[2])
edges=grafo['arestas']
for v in grafo['vertices']:
  menor=10000
  cand=None
  for e in edges:
    u,w,p = e
    if v in e:
      if p<menor:
        menor=p
        cand=e
  T.append(cand)
g=Plot(T,pos)
g.plot("Árvore Geradora Mínima - Boruvka")