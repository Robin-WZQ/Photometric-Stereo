import numpy as np
import scipy
import cv2

def compute_depth(mask,N):
    """
    计算出深度图
    """
    im_h, im_w = mask.shape
    N = np.reshape(N, (im_h, im_w, 3))

    # =================得到掩膜图像非零值索引=================
    obj_h, obj_w = np.where(mask != 0)
    no_pix = np.size(obj_h) #37244
    full2obj = np.zeros((im_h, im_w))
    for idx in range(np.size(obj_h)):
        full2obj[obj_h[idx], obj_w[idx]] = idx

    M = scipy.sparse.lil_matrix((2*no_pix, no_pix))
    v = np.zeros((2*no_pix, 1))

    # =================填充M和v=================
    for idx in range(no_pix):
        # 获取2D图像上的坐标
        h = obj_h[idx]
        w = obj_w[idx]
        # 获取表面法线
        n_x = N[h, w, 0]
        n_y = N[h, w, 1]
        n_z = N[h, w, 2]
        
        row_idx = idx * 2
        if mask[h, w+1]:
            idx_horiz = full2obj[h, w+1]
            M[row_idx, idx] = -1
            M[row_idx, idx_horiz] = 1
            if n_z==0:
                v[row_idx] = 0
            else:
                v[row_idx] = -n_x / n_z
        elif mask[h, w-1]:
            idx_horiz = full2obj[h, w-1]
            M[row_idx, idx_horiz] = -1
            M[row_idx, idx] = 1
            if n_z==0:
                v[row_idx] = 0
            else:
                v[row_idx] = -n_x / n_z

        row_idx = idx * 2 + 1
        if mask[h+1, w]:
            idx_vert = full2obj[h+1, w]
            M[row_idx, idx] = 1
            M[row_idx, idx_vert] = -1
            if n_z==0:
                v[row_idx] = 0
            else:
                v[row_idx] = -n_y / n_z
        elif mask[h-1, w]:
            idx_vert = full2obj[h-1, w]
            M[row_idx, idx_vert] = 1
            M[row_idx, idx] = -1
            if n_z==0:
                v[row_idx] = 0
            else:
                v[row_idx] = -n_y / n_z

    # =================求解线性方程组 Mz = v=================
    MtM = M.T @ M
    Mtv = M.T @ v
    z = scipy.sparse.linalg.spsolve(MtM, Mtv)

    std_z = np.std(z, ddof=1)
    mean_z = np.mean(z)
    z_zscore = (z - mean_z) / std_z
    outlier_ind = np.abs(z_zscore) > 10
    z_min = np.min(z[~outlier_ind])
    z_max = np.max(z[~outlier_ind])

    Z = mask.astype('float')
    for idx in range(no_pix):
        # 2D图像中的位置
        h = obj_h[idx]
        w = obj_w[idx]
        Z[h, w] = (z[idx] - z_min) / (z_max - z_min) * 255

    depth = Z
    return depth

def save_depthmap(depth,filename=None):
    """将深度图保存为npy格式"""
    if filename is None:
        raise ValueError("filename is None")
    np.save(filename, depth)

def disp_depthmap(depth=None, delay=0, name=None):
    """显示深度图"""
    depth = np.uint8(depth)
    if name is None:
        name = 'depth map'
    cv2.imshow(name, depth)
    cv2.waitKey()
    cv2.destroyAllWindows()
