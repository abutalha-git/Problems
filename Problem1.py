import numpy as np

def check(arr,key,i,j,k ):

    if k == k_len-1:
        return True
    try:
        if arr[i+1][j] == Key[k+1]:
            arr[i+1][j] = '0'
            return check(arr,key,i+1,j,k+1)
    except:
        pass
    try:
        if arr[i][j+1] == Key[k+1]:
            arr[i][j+1] = '0'
            return check(arr,key,i,j+1,k+1)
    except:
        pass
    try:
        if arr[i-1][j] == Key[k+1]:
            arr[i-1][j] = '0'
            return check(arr,key,i-1,j,k+1)
    except:
        pass
    try:
        if arr[i][j-1] == Key[k+1]:
            arr[i][j-1] = '0'
            return check(arr,key,i,j-1,k+1)
    except:
        pass
    return False





arr = [['A','B','C','E'],
       ['S','F','C','S'],
       ['A','D','E','E']]
Key = 'ABCB'
k_len = len(Key)
found = False
i_len = len(arr)
for k in range(0,k_len):
    for i in range(0,i_len):
        j_len = len(arr[i])
        for j in range(0,j_len):
              if arr[i][j] == Key[k]:
                   result = check(arr,Key,i,j,k)

print(result)
