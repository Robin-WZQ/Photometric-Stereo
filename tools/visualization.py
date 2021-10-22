import scipy.io as sio
import numpy as np

def visualize(file_path,class_name):
    depth = np.load(file_path)
    r, c = depth.shape

    f = open("results/obj files/"+class_name+'.obj', 'w')

    for i in range(r):
        for j in range(c):
            if depth[i, j] > 0:
                seq = 'v' + ' ' + str(float(i)) + ' ' + str(float(j)) + ' ' + str(depth[i, j]) + '\n'
                f.writelines(seq)

    f.close()
