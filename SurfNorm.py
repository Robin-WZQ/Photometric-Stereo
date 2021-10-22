import numpy as np
from sklearn.preprocessing import normalize

def compute_surfNorm(I, L, mask):
    '''物体表面法向量计算'''
    N = np.linalg.lstsq(L, I, rcond=-1)[0].T
    N = normalize(N, axis=1)    
    return N

def show_surfNorm(img,steps=3):
    height,width,_ = img.shape
    dst=np.zeros((height,width,3),np.float64)
    for i in range(3):
        for x in range(0,height,steps):
            for y in range(0,width,steps):
                dst[x][y][i]=img[x][y][i]

    return dst