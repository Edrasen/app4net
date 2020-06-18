
def partition(arr,low,high):
    #print(arr) 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]
  
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 ) 
  
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
        # part is partitioning index, arr[p] is now 
        # at right place 
        part = partition(arr,low,high) 
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, part-1) 
        quickSort(arr, part+1, high) 
  

