n = 4
Result = [None]*n

def DauNgoacDung(k):
    if UCV('(', k):
        Result[k] = '('
        if k == n-1:
            PrintResult()
        else:
            DauNgoacDung(k+1)

    if UCV(')', k):
        Result[k] = ')'
        if k == n - 1:
            PrintResult()
        else:
            DauNgoacDung(k + 1)


def UCV(c, k):
    t = 0
    for x in Result[:k]:
        if x == '(':
            t += 1
        else:
            t -= 1
        if t < 0:
            return 0
    if c == '(':
        t += 1
        if t < 0:
            return 0
        if k == n-1 and t != 0:
            return 0
    else:
        t -= 1
        if t < 0:
            return 0
        if k == n-1 and t != 0:
            return 0
    return 1

def PrintResult():
    print(*Result)

DauNgoacDung(0)