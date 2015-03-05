'''
Coursera: Stanford Algotithm Part I
Programming Question 1: Merge Sort and Count Number Inversions
Author: Jihong
Date: March 2015
'''


def loadData(filename):
    with open(filename) as f:
        lines = [x.split() for x in f]  # a list of lists
    f.close()

    tempList =  zip(*lines)             # a list of tuples := transposed lines
    tempList = list(tempList[0])        # a list of strings
    A = map(int,tempList)               # a list of integers
    
    return A


def mergeSort(A):
    if len(A) == 1:
        sortedA = A
    elif len(A)>1:
        LH = A[:len(A)//2]
        sortedLH = mergeSort(LH)
        RH = A[len(A)//2:]
        sortedRH = mergeSort(RH)
        sortedA = [0]*len(A) # initialise a list of length n
#        Merge
        i = 0   # mark of sortedLH
        j = 0   # mark of sortedRH
        k = 0   # mark of sortedA
#        both sortedLH and sortedRH are ergodic
        while i<len(sortedLH) and j<len(sortedRH):
            if sortedLH[i]<sortedRH[j]:
                sortedA[k]=sortedLH[i]
                i=i+1
            else:
                sortedA[k]=sortedRH[j]
                j=j+1
            k=k+1
#        sortedRH is ergodic
        while i<len(sortedLH):
            sortedA[k]=sortedLH[i]
            i=i+1
            k=k+1
#        sortedLH is ergodic
        while j<len(sortedRH):
            sortedA[k]=sortedRH[j]
            j=j+1
            k=k+1 

    return sortedA
    

def CountSplitInv(A,n):
    if len(A) <= 1:
        sortedA = A
        numInv = 0
    else:
        LH = A[:len(A)//2]
        sortedLH = mergeSort(LH)
        RH = A[len(A)//2:]
        sortedRH = mergeSort(RH)
        sortedA = [None]*len(A) # initialise a list of length n
        # Merge (Important: end cases)
        i = 0
        j = 0
        k = 0
        numInv = 0
        while i<len(sortedLH) and j<len(sortedRH):
            if sortedLH[i]<=sortedRH[j]:
                sortedA[k]=sortedLH[i]
                i=i+1
            elif sortedLH[i]>sortedRH[j]:
                sortedA[k]=sortedRH[j]
                j=j+1
                numInv = numInv + len(sortedLH)-i
            k=k+1
        

        while i<len(sortedLH):
            sortedA[k]=sortedLH[i]
            i=i+1
            k=k+1

        while j<len(sortedRH):
            sortedA[k]=sortedRH[j]
            j=j+1
            k=k+1 
    
    return (sortedA, numInv)


def Count(A, n):
    if n==1:
        return (A,0)
    elif n>1:
        LH = A[:n//2]
        RH = A[n//2:]
        (B,x) = Count(LH,len(LH))
        (C,y) = Count(RH,len(RH))
        (D,z) = CountSplitInv(A,n)
        return (D,x+y+z)
    

def main():
#    unit tests
#    A = loadData('test.txt')
#    print 'orginal: ', A
#    A = mergeSort(A)
#    print 'sorted: ', A

    A = loadData('IntegerArray.txt')
    (A,numInv) = Count(A, len(A))
    print 'Number inversions: %d' % numInv
 


if __name__ == "__main__":
	  main()
