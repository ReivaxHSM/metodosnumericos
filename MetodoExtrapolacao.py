#Modelmaneto matemático por regressão quadrática
# Autor: Heráclito S. M. Xavier
# Data: 2018-08-30
# Versão: 0.0.1
# Descrição: Este programa tem como objetivo realizar a extrapolação quadrática de dados de uma situação-problema
#            de forma a obter uma função que descreva o comportamento dos dados. A partir desta função, é possível
#            realizar a previsão de valores futuros.    
# --------------------------------------------------------------------------------------------------------------
#Dados de entrada:x (tempo em microssegundos) 0, 5, 10; y (amplitude em mm) 0, 2,846954, 1,795416 

# Vamos realizar o modelmaneto matemático da onda para um função do tipo y = a*x**2 + b*x + c
# Identificar a ampltude da pmda y no instante x = 1 microssegundo

# Regressão quadrática
# importando as bibliotecas

from numpy import matrix, linalg
import numpy as np

# Inserindo as coordenadas dos pontos da tabela
x0 = 0
y0 = 0

x1 = 5
y1 = 2.846954

x2 = 10
y2 = 1.795416

m = 3 # número de pontos

# Determinando as somas que compo~em a matriz
print("Para determinar a função y=a0+a1*x+a2*x**2")

soma1=x0+x1+x2
soma2=(x0*x0)+(x1*x1)+(x2*x2)
soma3=(x0*x0*x0)+(x1*x1*x1)+(x2*x2*x2)
soma4=(x0*x0*x0*x0)+(x1*x1*x1*x1)+(x2*x2*x2*x2)

soma5=y0+y1+y2
soma6=(x0*y0)+(x1*y1)+(x2*y2)
soma7=((x0*x0)*y0)+((x1*x1)*y1)+((x2*x2)*y2)

# Apresentando o sistema matricial do método
print("A*X=B")
matriz_A=matrix([[m,soma1,soma2],[soma1,soma2,soma3],[soma2,soma3,soma4]])
matriz_B=matrix([[soma5],[soma6],[soma7]])
print("Matriz A")
print(matriz_A)
print("Matriz B")
print(matriz_B)

#Resolvendo o sistema para determinar os coeficientes pela Regra de Craemer
print()
print("Determinando os coeficientes pela Regra de Craemer")
det_A=linalg.det(matriz_A)
print("Determinante da matriz A")
print(det_A)
print()
print("Determinando os coeficientes")
a0=linalg.det(matrix([[soma5,soma1,soma2],[soma6,soma2,soma3],[soma7,soma3,soma4]]))/det_A
a1=linalg.det(matrix([[m,soma5,soma2],[soma1,soma6,soma3],[soma2,soma7,soma4]]))/det_A
a2=linalg.det(matrix([[m,soma1,soma5],[soma1,soma2,soma6],[soma2,soma3,soma7]]))/det_A
print()
print("Coeficientes")
print()
print("a0=",a0)
print("a1=",a1)
print("a2=",a2)

#Apresentando a função de segundo grau
print()
print("A função intermpoladora é dada por:")
print("y = ",a0," + ",a1,"x + ",a2,"x\u00B2")
print()

# Finalizando o programa
print("Fim do programa")
print("Obrigado por utilizar o programa")
print("Autor: Heráclito S. M. Xavier")
print("Data: 2018-08-30")
print("Versão: 0.0.1")
print("E-mail:contato@educadorxavier.com.br")
print("Site: www.educadorxavier.com.br")
print("Facebook: www.facebook.com/educadorxavier")
print("Instagram: www.instagram.com/educadorxavier")
print("Twitter: www.twitter.com/educadorxavier")
print("Youtube: www.youtube.com/educadorxavier")
print("Github: https://github.com/ReivaxHSM/Python")



