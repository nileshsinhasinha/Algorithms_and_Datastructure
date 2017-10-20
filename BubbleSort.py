"""Bubble sorting :- It will sort the string by comparing adjacent element and swapping the values if right
                     side is a larger value"""

def bubble_sort(Arr):
    length = len(Arr)
    for i in range(length):
        Swapped = 0
        for j in range(length-i-1):
            if Arr[j] > Arr[j+1]:
                Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
                Swapped=1
        if Swapped==0:
            break

if __name__ == "__main__":
    a=[25,10]
    bubble_sort(a)
    print(a)

