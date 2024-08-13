
from SortingClass import SortingClass


# def mergeSorting (a):
#     unsorted = True
#     while unsorted:
        
    
#     return a


# def main ():
#     unsortedArray = [3,8,2,6,1,4,5,9,7,13]
#     sortedArray = mergeSorting (unsortedArray)
#     print (sortedArray)

def main ():
    order = ["asc", "desc"]
    unsortedArray = [3,8,2,6,1,4,5,9,7,13]
    unsortedArray2 = ['c','a', 'z', 'pk','h']
    sorting = SortingClass()
    sortedArray = sorting.bubbleSorting (unsortedArray, order[0])
    sortedArray2 = sorting.bubbleSorting (unsortedArray2, order[1])
    print (sortedArray)
    print (sortedArray2)

main ()