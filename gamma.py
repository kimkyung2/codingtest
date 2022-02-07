import numpy as np
import pandas as pd

def chol_solve(K):
	a = np.linalg.eig(K)[1] #vector
	b = np.linalg.eig(K)[0] #values
	print(b)
	b[b<1e-13] = 1e-13
	b = 1/np.sqrt(b)
	print(a)
	return np.matmul(np.matmul(a, np.diag(b)), np.transpose(a))


def rotate(Y, sigma):
	U = chol_solve(sigma)
	tU = np.transpose(U)
	UY = np.matmul(tU, Y)
	return UY

Xpath = open("./testData/X_rightdim.txt")
Ypath = open("./testData/Y_rightdim.txt")
Kpath = open("./testData/K.txt")
VCpath = open("./testData/VC.txt")
#X = np.array(pd.read_table(Xpath, header=None))
#Y = np.array(pd.read_table(Ypath, header=None))
#K = np.array(pd.read_table(Kpath, header=None))
X = np.loadtxt(Xpath, dtype="float")
Y = np.loadtxt(Ypath, dtype="float")
K = np.loadtxt(Kpath, dtype="float")
VC = np.array(pd.read_table(VCpath, header=None))
snpNum = X.shape[1]
indiNum = X.shape[0]
geneNum = Y.shape[1]
Vg = round(np.median(VC[:,0]),6)
Ve = np.median(VC[:,1])
I = np.eye(indiNum, dtype=float)
sigma = np.multiply(Ve, I) + np.multiply(Vg, K)
#print(sigma)

UY = rotate(Y,sigma)
#UX = rotate(X,sigma)
#print(UY)
#print(UX)






Xpath.close()
Ypath.close()
Kpath.close()
VCpath.close()




