# Photometric-Stereo
A python implementation of the Basic Photometric Stereo Algorithm

## Result

(a) noraml vector

(b) depth map

(c) point cloud picture (observed from the front view)

(d) point cloud picture (observed from the side view) [By Meshlab]

![图片1](%E5%9B%BE%E7%89%871.png)

![图片2](%E5%9B%BE%E7%89%872.png)


## Usage

run Photometric_Stereo.py

## Code Tree

|data  #raw data，tga format

|data_processed  #processed data，png format

|results

-----|normal files  # noraml vector pictures

-----|obj files  # 3D point cloud image

|tools

-----|tga2png.py  #tga2png function

-----|visualization.py  # point cloud visualize function

est_depth.npy  #the numpy file of point cloud

HeightMap.py  #set of height map computed functions

Photometric_Stereo.py  # main function

README.md # description file

requirements.txt  # dependence

SurfNorm.py # set of surface noraml vector computed functions

## Reference
借鉴大神的博客
https://blog.csdn.net/SZU_Kwong/article/details/112757354
