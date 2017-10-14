"Insertion Sort -  Inplace algorithm"


# Space complexity = O(1)
def insertion_sort(n_input):
    "It will compare A[i] with A[j] if A[j]>A[i] will swap it"
    for j in range(1, len(n_input)):
        key = n_input[j]  # To hold the value in case of swaping
        # insert A[j] into sorted sequence A[1...j-1]
        i = j - 1
        while i >= 0 and n_input[i] > key:
            n_input[i + 1] = n_input[i]
            i = i - 1
        n_input[i + 1] = key
    return n_input
