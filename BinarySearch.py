def BinarySearch(A, start ,end , y):
    mid = (end+start)//2
    if A[mid] == y:
        return mid
    else:
        if A[mid] > y:
            return BinarySearch(A, start, mid-1, y)
        else:
            return BinarySearch(A, mid+1, end, y)

A = [1,2,3,4,5,7,8,23,45]
print(BinarySearch(A,0,8,7))