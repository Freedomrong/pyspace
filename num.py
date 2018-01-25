#!/usr/bin/env python3
import numpy as np

#向np.array()中传入一个python列表，dtype制定了生成的数组的数据长度和类型
array = np.array([1,2,3], dtype = np.uint8)
print(array)

#快速创建一个两行三列的全0矩阵
mat1 = np.zeros((2,3))
print(mat1)

#创建一个1*2*3*4尺寸的高维矩阵
nd = np.zeros((1,2,3,4))
print(nd.shape)
print(nd.size)

#标量与矩阵相乘
scalar = 2
mat = np.zeros((2,3))
mat1 = scalar*mat
print(mat1)

#矩阵转置
mat = np.zeros((2,3))
tmat = mat.T                   #.T即可得到其转置
print(mat.shape, tmat.shape)
mat3 = np.array((1,2,3))
tmat = mat.T
print(mat3.shape, tmat.shape)

#矩阵相加
mat1 = np.array([[1,2],[3,4]])
mat2 = np.array([[1,0],[0,1]])
mat3 = mat1 + mat2
print(mat3)

#矩阵乘法
mat1 = np.array([[1,2],[3,4]])
mat2 = np.array([[1,0],[0,1]])
mat3 = mat1.dot(mat2)           #矩阵乘法通过.dot()函数实现
print(mat3)
