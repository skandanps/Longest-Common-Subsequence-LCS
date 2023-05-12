import time
	
def lcs(X, Y, m, n):
	if(m == 0 or n == 0):
		return 0 
	
	if(X[m-1] == Y[n-1]):
		return lcs(X, Y, m-1, n-1)+1 		
	else :
		return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)) 
	 
	
def readFile(file):
    lines = []
    with open(file) as f:
        lines= f.readlines()
    return lines 

fileName = "LCS1.txt"
strings = readFile(fileName)
t = []
for i in range(0, len(strings), 1): 
    inputStrings = strings[i].split(",")
    if(len(inputStrings) > 0):
        start_time = time.time()
    
        length = lcs(inputStrings[0], inputStrings[1], len(inputStrings[0]), len(inputStrings[1]))
        end_time = time.time()
        print()
        print("##########################################################")
        print("Length of the Longest common Subsequence of Strings {} & {} is {} ".format(inputStrings[0], inputStrings[1], length))
        print("Time taken to find length of longest common subsequence is : {} seconds".format(end_time-start_time))
        t.append(end_time-start_time)
        print("##########################################################")
        print()

for i in range (0, len(t), 1):
    print(t[i])