import numpy as np
#Suma de matrices
E = np.array([[60,70],
              [40,50],
              [30,60]]) * 0.9

M = np.array([[70,80],
              [60,50],
              [20,40]]) *1.3
     

K = np.array([[0,0],
     [0,0],
     [0,0]])

for i in range(len(E)):
  for j in range(len(E[0])):
    K[i][j]  = E[i][j] + M[i][j]
#print(K)
#Multiplicación de matrices
A = np.array([[60,70],
              [40,50],
              [30,60]])

B = np.array([[70,80],
              [60,50],
              [20,40]])
#C = np.dot(A,B)
#print(C)
#Voltear matrices 
A = np.array([[2,5,9],[0,7,11]])
B = np.transpose(A)
print(B)

C = A.dot(B)
#print(C)