'''
    @file_name:Photometric_Stereo
    @file_function: Photometric Stereo algorathim
    @time: 2021/9/24
    @author: Wang Zhongqi
    @software: VSCode 
'''
import cv2
import numpy as np
from PIL import Image

from HeightMap import compute_depth, disp_depthmap, save_depthmap
from SurfNorm import compute_surfNorm
from tools.visualization import visualize


def main(Image_name = 'cat'):

    # =================read the information in MASK=================
    mask = cv2.imread('data_processed/'+Image_name+"/"+Image_name+'.mask.png')
    mask2 = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    height,width,_=mask.shape
    dst=np.zeros((height,width,3),np.uint8)
    for k in range(3):
        for i in range(height):
            for j in range(width):
                dst[i,j][k]=255-mask[i,j][k]

    # ================obtain the light vector=================
    file_path = "data_processed/lights.txt"
    file = open(file_path,'r')
    L=[]
    i=0
    while 1:
        line = file.readline()
        if not line:
            break
        if(i!=0):
            line = line.split(" ")
            line[2] = line[2].replace("\n",'')
            for l in range(3):
                line[l] = float(line[l])
            L.append(tuple(line))
        i+=1
    file.close()
    L = np.array(L)

    # =================obtain picture infor=================
    I = []
    for i in range(12):
        picture = np.array(Image.open('data_processed/'+Image_name+"/"+Image_name+'.'+str(i)+'.png'),'f')
        picture = cv2.cvtColor(picture,cv2.COLOR_RGB2GRAY)
        height, width = picture.shape #(340, 512)
        picture = picture.reshape((-1,1)).squeeze(1)
        I.append(picture)
    I = np.array(I)

    # =================compute surface normal vector=================
    normal = compute_surfNorm(I, L,mask)
    N = np.reshape(normal.copy(),(height, width, 3))
    # RGB to BGR
    N[:,:,0], N[:,:,2] = N[:,:,2], N[:,:,0].copy()
    N = (N + 1.0) / 2.0
    result = N + dst
    cv2.imshow('normal map', result)
    cv2.waitKey()
    cv2.destroyAllWindows()    
    result = result * 255
    cv2.imwrite("results/normal files/"+Image_name+".jpg",result)

    # =================compute depth map=================
    Z = compute_depth(mask=mask2.copy(),N=normal.copy())
    save_depthmap(Z,filename="./est_depth")
    disp_depthmap(depth=Z,name="height")

    # =================generate the obj file to visualize=================
    visualize('est_depth.npy',Image_name)
    
if __name__ == "__main__":
    things = ["buddha","gray",'cat','gray','horse','owl','rock']
    i=0
    for thing in things:
        i+=1
        print("progress：{}/{}".format(i,len(things)))
        main(thing)
