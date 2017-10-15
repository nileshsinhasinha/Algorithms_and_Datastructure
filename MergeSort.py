def merging(arr,strt,mid,end):
    import math
    inf = math.inf
    n1 = mid-strt+1
    n2 = end-mid
    lft=arr[strt:n1]
    rght=arr[n2:end]
    lft.append(inf)
    rght.append(inf)
    #print(lft)
    #print(rght)
    i=0
    j=0
    for k in range(strt,end):
        if lft[i] <= rght[j]:
            arr[k] = lft[i]
            i=i+1
        else:
            arr[k]=rght[j]
            j=j+1
    return(arr)


def merge_sort_main(arr):
    strt=0
    end=len(arr)
    mid=0
    merge_sort(arr,strt,end)
    return arr

def merge_sort(arr,strt,end):
    if strt<end:
        mid=(strt+end)//2
        merge_sort(arr,strt,mid)
        merge_sort(arr,mid+1,end)
        merging(arr,strt,mid,end)
        print(arr)


#print(merge_sort_main([1,2,3,8,8,2,7,8]))
print(merging([1,5,7,8,2,4,6,9],0,4,8))
