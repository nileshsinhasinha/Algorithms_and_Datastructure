def partition(arr, left_index, right_index):
    """Picks the last element as pivot and partition the element around
    pivot(left side -->less than equal to pivot
          right side --> greater than equal to pivot)"""

    x_pivot = arr[right_index]
    i_left = left_index

    for j_right in range(left_index, right_index):
        if arr[j_right] <= x_pivot:
            arr[i_left],arr[j_right] = arr[j_right],arr[i_left]
            i_left += 1

    arr[i_left],arr[right_index] = x_pivot,arr[i_left]
    return i_left


def quicksort_main(arr, left, right):
    """
    Quick sort method (Recursive)
    """
    if (right-left) > 0:
        # Get pivot
        piv = partition(arr, left, right)
        # Sort left side of pivot
        quicksort_main(arr, left, piv - 1)
        # Sort right side of pivot
        quicksort_main(arr, piv + 1, right)

def quicksort(arr):
    """To call the function with single parameter array"""
    left=0
    right=len(arr)-1
    quicksort_main(arr,left,right)
    return arr

if __name__ == "__main__":
    print(quicksort([6,2]))
