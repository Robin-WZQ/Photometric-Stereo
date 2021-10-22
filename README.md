# Photometric-Stereo
A python implementation of the Basic Photometric Stereo Algorithm

## Result

![图片1](%E5%9B%BE%E7%89%871.png)

![图片2](%E5%9B%BE%E7%89%872.png)

## Usage

run Photometric_Stereo.py

## Code Tree

|data  #原始数据，tga格式

|data_processed  #处理后的数据，png格式

|results

-----|normal files  #法向量图片

-----|obj files  #3维点云图

|tools

-----|tga2png.py  #tga格式转png格式工具函数

-----|visualization.py  #点云可视化生成工具

est_depth.npy  #点云的numpy格式文件

HeightMap.py  #高度场计算函数集合

Photometric_Stereo.py  #主函数

README.md #说明文件

requirements.txt  #所需要的第三方库

SurfNorm.py #物体表面法向量计算函数集合

