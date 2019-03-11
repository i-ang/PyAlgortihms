def insert(A):
    for i in range(0,len(A)):
        curVal = A[i] #at the start, A[i] = 4 
        j = i - 1
        while j>=0:
            if curVal < A[j]: #A[j] at the start is 5 
                A[j+1] = A[j]
                A[j] = curVal
                j = j - 1
                print(A)
            else:
                break

A = [5,4,3,2,1]
insert(A)
#print(A)
            
