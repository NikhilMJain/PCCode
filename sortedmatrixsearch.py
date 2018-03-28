mat = [[10, 20, 30, 40], [15, 25, 35, 45], [26, 36, 46, 56], [71, 81, 91, 98]]

key = 56

def searchmat():
    i = 0
    j = l = len(mat) - 1
    while i>=0 and j>=0 and i<=l and j<=l:
        if mat[i][j] == key:
            return i, j
        if mat[i][j] > key:
            j = j - 1
        else:
            i = i + 1
    return False

print searchmat()