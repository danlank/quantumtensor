import numpy as np
import sys 
from numba.typed import List

def vec_to_mps (vect,N):
    b=vect.reshape(1,2**N)
    nps_list=List()
    for i in range(N):
        dims=np.asarray(b.shape)
        d2=int(dims[1]/2)
        mat=b.reshape(dims[0],2,d2)
        mat2=mat.reshape(dims[0]*2,d2)
        u,s,v=np.linalg.svd(mat2,full_matrices=False)
        b=np.diag(s) @ v
        dims=np.asarray(u.shape)
        d3=int(dims[0]/2)
        u=u.reshape(d3,2,dims[1])
        nps_list.append(u)
        return nps_list
        
        
N=4
site = 1
vect = np.zeros(2**N, dtype=np.complex128) 
vect[site] = 1

MPS = vec_to_mps(vect, N)
print(MPS, end='\n\n')
