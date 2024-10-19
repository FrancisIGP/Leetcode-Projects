# bubble sort algorithm

number_set = [2, 3, 4, 10, 9, 11, 15, 1]

def bubble_sort(arr):

    for ctr1 in range(len(arr) - 1, 0, -1):
        
        for ctr2 in range(ctr1):
            if arr[ctr2] > arr[ctr2 + 1]:
                sorted = True
                arr[ctr2], arr[ctr2 + 1] = arr[ctr2 + 1], arr[ctr2]
            
    return print(arr)    
                
bubble_sort(number_set)