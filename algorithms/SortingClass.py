

class SortingClass ():
    def __init__ (self):
        pass
    
    def bubbleSorting (array, order):
    
        for i in range (0, len(array)):
            for j in range (i+1, len(array)):
                if order == "asc":
                    if array [i] > array [j]:
                        array[i], array[j] = array[j], array[i]
                else:
                    if array [i] < array [j]:
                        array[i], array[j] = array[j], array[i]
                
        return array