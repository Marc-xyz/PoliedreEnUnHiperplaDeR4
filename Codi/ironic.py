#!/usr/bin/env pythfor m
# -*- coding: utf-8 -*-

#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+
#+  10/12/2019                                              Geometria lineal  #+
#+                                                                            #+
#+          Programa_1 per determinar quins vèrtexs                           #+
#+          pertanyen a  cada cara del poliedre.                              #+
#+                                                                            #+
#+   *Els primers dos comentaris són necessaris per imprimir accents          #+
#+                                                                            #+
#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+


def caretal_programa1():
    print("#+"*40)
    print("#+" + "  "*1 + "10/12/2019" +  " "*46 + "Geometria lineal  "+ "#+")
    print("#+" + "  "*38 + "#+")
    print("#+" + "  "*5 + "Programa per determinar quins vèrtexs" +  " "*29 + "#+")
    print("#+" + "  "*5 + "pertanyen a  cada cara del poliedre." +  " "*30 + "#+")
    print("#+" + "  "*38 +"#+")
    print("#+"*40)
   
caretal_programa1()   
#Llista amb les coordenades dels vèrtex del poliedre com a punts de R^4
vertex=[(4,1,2,3),
          (3,1,2,4),
          (3,2,1,4),
          (4,2,1,3),

          (1,4,1,4),
          (1,6,1,2),
          (1,6,2,1),
          (1,2,6,1),

          (2,1,6,1),
          (4,1,4,1),
          (2,1,3,4),
          (1,2,3,4),

          (4,3,2,1),
          (4,3,1,2)]
#Llista amb les equacions del hiperplans com a "vectors" (c_x,c_y,c_z,c_t)
hipers=[(3,-1,-1,-1,6),
        (-1,3,-1,-1,6),
        (-1,-1,3,-1,6),

        (-1,-1,-1,3,6),
        (1,1,-1,-1,4),
        (-1,1,1,-1,4),

        (-1,-1,1,1,4),
        (1,1,1,-3,6),
        (-3,1,1,1,6),]
#En aquesta llista guardarem els vèrtex de cada cara (com a nom):
relacions=[]
#En aquesta llista guardarem els vèrtex de cada cara (de forma explicita):
relacionsExplicit=[]
# 9 cares del poliedre
for i in range(9):
    nameOfList="H_"+str(i+1)+":"
    relacions.append([nameOfList,])
    relacionsExplicit.append([nameOfList,])
# 14 cares del poliedre
    for j in range(14):
        sum=0
        for k in range(4):
            sum+=vertex[j][k]*hipers[i][k]
        sum=sum+hipers[i][4]
        if(sum==0):
            (relacions[i]).append("V_{"+str(j+1)+"}")
            (relacionsExplicit[i]).append(vertex[j])
print("\n")
# Solucions Implicites
print("Solucions en format implicit: ")
for epsilon in range(9):
    print(relacions[epsilon])
print("\n")
#Solucions Explicites
print("Solucions en format explicits: ")
for epsilon in range(9):
    print(relacionsExplicit[epsilon])
print("\n")
