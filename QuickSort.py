def partition(arr):
    if len(arr)<2:
        return 0

    x_pivot = arr[len(arr)-1]

    i_left=-1

    for j_right in range(len(arr)-1):
        if arr[j_right] <= x_pivot:
            i_left+=1
            intmdt=arr[i_left]
            arr[i_left]=arr[j_right]
            arr[j_right]=intmdt

    intmdt=arr[i_left+1]
    arr[i_left+1]=x_pivot
    arr[len(arr)-1] = intmdt
    return i_left+1

#print(partition([5]))

def quicksort(arr):
    #print('L>>{}'.format(len(arr)))
    if len(arr)>0:
            #return arr

        q=partition(arr)
        #print('Q>>{}'.format(q))
        quicksort(arr[:q])
        #print(arr)
        quicksort(arr[(q+1):])
        #print(arr)
    return arr

if __name__ == "__main__":
    print(quicksort([6,9,5,0]))

print(partition([6,5,0,8]))


