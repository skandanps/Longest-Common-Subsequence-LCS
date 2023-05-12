import time
import numpy as np
	
def lcs(X, Y):
    start_time = time.perf_counter()
    m = len(X)
    n = len(Y)
    L = [[0 for i in range(n+1)] for j in range(m+1)]
    M = [[" " for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0 
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
                M[i][j] = fr"\{''}"
            elif L[i-1][j] >= L[i][j-1]:
                L[i][j] = L[i-1][j]
                M[i][j] = "^"
            else:
                L[i][j] = L[i][j-1]
                M[i][j] = "<"
    lcs = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs += X[i-1]
            i -= 1
            j -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1          
        else:
            j -= 1
    lcs = lcs[::-1]
    print_bc_array(L,M,X,Y,lcs)
    end_time = time.perf_counter()

def print_LCS(b, X, i, j):
    if(i == 0 or j == 0):
        return
    if(b[i][j] == fr"\{''}"):
        print_LCS(b, X, i-1, j-1)
        print(X[i])
    elif(b[i][j] == "^"):
        print_LCS(b, X, i-1, j)
    else:
        print_LCS(b, X, i, j-1)
    
def readFile(file):
    lines = []
    with open(file) as f:
        lines= f.readlines()
    return lines


def print_bc_array(b,c,X,Y,lcs):
    len_x = len(X)
    len_y = len(Y)
    x = "X" + X
    x = " "+x
    y = "Y" + Y
    new_row = list(y)
    new_x = list(x)
    arr = np.array(b,dtype=object)
    arr = np.insert(arr,0,new_row, axis=0)
    arr = arr.tolist()

    arr2 = np.array(c,dtype=object)
    arr2 = np.insert(arr2,0," ", axis=0)
    arr2 = arr2.tolist()

    for i in range(len(arr2)):
        arr2[i] += " "

    for i in range(len(x)):
        var = new_x[i]
        arr[i].insert(0,var)

    m = len(x)
    n = len(y) +1

    print("#####################################################")
    for i in range(0,m):
        for j in range(0,n):
            print(arr[i][j], arr2[i][j],end =" ")
        print()
    print("#####################################################")
    length_of_longest_common_subsequence = len(lcs)
    longest_common_sub_sequence = lcs
    print("Length of longest common subsequence is : {}".format(length_of_longest_common_subsequence))
    print("The longest common subsequence of given strings {} and {} is {}".format(str( x [2:] ), str( y[ 1:]), lcs))
    print()

fileName = "LCS2.txt"
strings = readFile(fileName)

for i in range(0, len(strings), 1): 
    inputStrings = strings[i].split(",")
    if(len(inputStrings) > 0):
        lcs(inputStrings[0], inputStrings[1])
        
        
    