import Heap as heap

def heapsort(Arr):
    """Sorting the given array in ascending order using heap data structure"""
    heap.build_max_heap(Arr)
    #print(Arr)
    new_arr=Arr[:]
    #node=0
    #while node
    for node in range(len(Arr)-1,0,-1):
        Arr[node],Arr[0],new_arr[node],new_arr[0]=new_arr[0],new_arr[node],new_arr[0],new_arr[node]
        #print('MH1>>{}{}'.format(Arr,new_arr))
        new_arr.pop()
        #print('MH2>>{}{}'.format(Arr,new_arr))
        heap.max_heapify(new_arr,0)
        #print('MH3>>{}{}'.format(Arr,new_arr))

if __name__ == "__main__":
    l=[40,30,20,10,15,16,17,8,4]
    heapsort(l)
    print(l)
