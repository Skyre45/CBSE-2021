# Helper functions used by the cbX*.py scripts (numpy / matplotlib only).
# Adapted from G. V. V. Sharma, {https://github.com/gadepall/matgeo/tree/main/codes/CoordGeo}
# (line/funcs.py, conics/funcs.py, plotting/funcs.py, triangle/funcs.py), released under GNU GPL.
# Keep this file in the same folder as the scripts.

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# 90 degree rotation matrix (normal vector from direction vector)
omat = np.array([[0, 1], [-1, 0]])

def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return omat@dir_vec(A,B)

def ang_vec(m1,m2):
    return np.arccos(((m1.T@m2)/(np.linalg.norm(m1)*np.linalg.norm(m2))).item())

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def line_gen_num(A,B,num):
  dim = A.shape[0]
  x_AB = np.zeros((dim,num))
  lam_1 = np.linspace(0,1,num)
  for i in range(num):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def line_intersect(n1,A1,n2,A2):
  N=np.block([n1,n2]).T
  p = np.zeros((2,1))
  p[0] = (n1.T@A1).item()
  p[1] = (n2.T@A2).item()
  #Intersection
  P=np.linalg.solve(N,p)
  return P

def perp_foot(n,c,P):
  m = omat@n
  N=np.block([m,n])
  p = np.zeros((2,1))
  p[0][0] = (m.T@P).item()
  p[1][0] = c
  #Intersection
  x_0=np.linalg.solve(N.T,p)
  return x_0

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ + O)
	return x_circ

def chord(V,u,f,m,h):
    #intermediate
    c = h.T@V@h+2*u.T@h+f 
    b = 2*m.T@(V@h+u)
    a = m.T@V@m
    k = np.roots((np.block([a,b,c])).flatten()).reshape(-1,1)
    Pmat = np.block([k,np.ones((2,1))]).T
    #print(Pmat,k)
    nmat = np.block([m,h])
    x = nmat@Pmat
    #x1 = h+k[0]*m
    #x2 = h+k[1]*m
    #return x1,x2
    return x

def label_pts(G_v,vert_labels): 
    for i, txt in enumerate(vert_labels):
        plt.annotate(txt, # this is the text
                     (G_v[0,i], G_v[1,i]), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     ha='center')

def tri_sides(A,B,C):
    a = LA.norm(B-C)
    b = LA.norm(C-A)
    c = LA.norm(A-B)
    return c,a,b

def icircle(A,B,C):
  k1 = 1
  k2 = 1
  p = np.zeros((2,1))
  t = norm_vec(B,C)
  n1 = t/LA.norm(t)
  t = norm_vec(C,A)
  n2 = t/LA.norm(t)
  t = norm_vec(A,B)
  n3 = t/LA.norm(t)
  p[0] = n1.T@B- k1*n2.T@C
  p[1] = n2.T@C- k2*n3.T@A
  #Intersection
  N1= n1 - k1 * n2
  N2= n2 - k1 * n3
  N=np.block([[N1.T],[N2.T]])
  I=LA.solve(N,p)
  r = n1.T@(I-B)
  return I,r

# evaluate a matrix polynomial (Horner), adapted from matgeo/codes/CoordGeo/matrix/funcs.py
def polyvalm(f, A):
    R = np.zeros_like(A, dtype=float)
    for c in f:
        R = R @ A + c * np.eye(A.shape[0])
    return R

