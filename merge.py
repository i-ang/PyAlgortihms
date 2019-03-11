def mergeSort(A):
    print("splitting..",A)
    
    if len(A)>1:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i = i + 1
            else:
                A[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            A[k] = left[i]
            i = i + 1
            k = k + 1
            
        while j < len(right):
            A[k] = right[j]
            j = j+ 1
            k = k + 1

    print("merging!",A)

A = [5,8,7,6,3,9,1,2,123,5,1,6,7,2,2,5,7,9,6]
mergeSort(A)
print(A)
