def memory_usage():
    import psutil
    import os
    import sys
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 10)
    return mem


def space_complexity(fn):
    import GraphicalAnalysis
    import random

    Input_X = []
    Space_per_input_Y = []
    for i in range(10,1001,100):
        N_input=[]
        M=0
        for j in range(i):
            N_input.append(random.randint(1,100000))
        Input_X.append(i)
        for i in range(100):
            m1=memory_usage()
            fn(N_input)
            m2=memory_usage()
            M+=(m2-m1)
        Space_per_input_Y.append((M))
    GraphicalAnalysis.singlegraph(Input_X,Space_per_input_Y,y_label='Space-->Bytes',title='Space Complexity')

# import InsertionSort
# space_complexity(InsertionSort.insertion_sort)
#
# import MergeSort
# space_complexity(MergeSort.mergesort)

# import QuickSort
# space_complexity(QuickSort.quicksort)

# import HeapSort
# space_complexity(HeapSort.heapsort)

import BubbleSort
space_complexity(BubbleSort.bubble_sort)

# m1=memory_usage()
# g=[i for i in range(1)]
# m2=memory_usage()
# print(m2-m1)
