def knapSack(W, wt, val, n):
    
	## A matrix of (W+1) columns and (n+1) rows
	K = [[0 for x in range(W + 1)] for x in range(n + 1)]

	## iterating through matrix
	for i in range(n + 1):
		for j in range(W + 1):
    			
			## j will act as current capacity (0 --> W)
    			
			## 0 capacity means we cant add any weight so 0 profit
			if i == 0 or j == 0:
				K[i][j] = 0

			## if current weight is less than capacity
			elif wt[i-1] <= j:
				K[i][j] = max(val[i-1] + K[i-1][j-wt[i-1]], K[i-1][j])
			
			## else consider the previous profit - means you did not take that weight in the knapsack
			else:
				K[i][j] = K[i-1][j]

	## return the bottom right profit - max possible profit
	return K[n][W]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print("Maximum total value : ", knapSack(W, wt, val, n))
