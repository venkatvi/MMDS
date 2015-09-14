import numpy as np; 
def pageRank(M, beta, eps):
	# requires M as array
	dims = M.shape;
	if dims[0] != dims[1]:
		print "Invalid stochastic matrix M";
	
	r = [1/dims[0]] * dims[0]; # initialize rank to 1/N

	# compute all out degrees  of nodes by summing columsn
	outDegree = M.sum(axis = 0);
	t = 1; 
	while True:
		rankTemp = [0] * dims[0];
		for i in range(dims[0]):
			rankTemp[i] = 0;
			# figure out all incoming nodes of node i; 
			for j in range(dims[1]):
				if M[i][j] == 1:
					rankTemp[i] = rankTemp[i] + (beta * (r[j]/outDegree[j])); 
		sumRank = sum(rankTemp);
		leakingRank = 3 - sumRank;
		leakingRankToAdd = leakingRank/dims[0];

		overallError = 0;
		for i in range(dims[0]):
			rankTemp[i] = rankTemp[i] + leakingRankToAdd;
			overallError = overallError + abs(rankTemp[i] - r[i]);

		r = rankTemp;
		if overallError < eps:
			break;
		t = t+1;
	return r;

if __name__ == "__main__":
	M = [[0, 0, 0], [1, 0, 0], [1, 1, 1]];
	M = np.array(M);                     
	r = pageRank(M, 0.7, 0.000001);
	print r




