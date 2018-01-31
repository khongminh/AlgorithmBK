A = [1,2,3]
B = [None] * len(A)

def HoanVi(k):
    for x in A:
        if UCV(x, k) == 1:
            B[k] = x
            if k == len(A)-1:
                PrintResult()
            else:
                HoanVi(k+1)

def UCV(x,k):
    for y in B[:k]:
        if x == y:
            return 0
    return 1

def PrintResult():
    print(*B)

HoanVi(0)