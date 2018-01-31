n = 8
result = [None]*(n+1)

def XepHau(k):
    for i in range(1,n+1):
        if UCV(i,k) == 1:
            result[k] = i
            if k == n:
                PrintResult()
            else:
                XepHau(k+1)



def UCV(i,k):
    for j in range(1,k):
        if result[j] == i or abs(result[j]-i) == k-j:
            return 0
    return 1


def PrintResult():
    print(*result[1:])

XepHau(1)