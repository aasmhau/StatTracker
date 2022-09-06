
"""
Sorting algorithms and theory

Stability is whether two elements of equal value stay in their original order
when sorted. 

Stable: Insertion, Merge, Counting, Radix, Bucket and Bubble
Unstable: Heap, Quick, Selection


"""

def bubbleSort(numList):
    length = len(numList)
    
    swap = True
    while(swap):
        swap = False
        i = 0
        while(i < length-1):
            if numList[i] > numList[i+1]:
                numList[i], numList[i+1] = numList[i+1], numList[i]
                swap = True
            i += 1

def insertionSort(numList):
    for i in range(1, len(numList)):
        current = numList[i]

        

if __name__ == "__main__":
    toBeSorted = [1,6,2,9,3,3,5]
    print(toBeSorted)

