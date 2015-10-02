import numpy as np 
def findLCS(LCS, X, Y, i, j):
	if (i <0 or j <0):
		return 0;
	if (X[i] == Y[j]):
		LCS[i][j] = findLCS(LCS, X, Y, i-1, j-1) + 1;
	else:
		if (LCS[i-1][j] == 0):
			LCS[i-1][j] = findLCS(LCS, X, Y, i-1, j);
		if (LCS[i][j-1] == 0):
			LCS[i][j-1] = findLCS(LCS, X, Y, i, j-1);
		LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1]);
	return LCS[i][j];

if __name__ == "__main__":
	X = "1234"
	Y = "122223232224"
	LCS = np.zeros((len(X), len(Y)));
	lenLCS = findLCS(LCS, X, Y, len(X)-1, len(Y)-1);
	print lenLCS