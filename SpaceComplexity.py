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
    for i in range(2,101,2):
        N_input=[]
        for j in range(i):
            N_input.append(random.randint(1,100000))
        Input_X.append(i)
        m1=memory_usage()
        fn(N_input)
        m2=memory_usage()
        Space_per_input_Y.append((m2-m1))
    GraphicalAnalysis.singlegraph(Input_X,Space_per_input_Y,y_label='Space-->Bytes',title='Space Complexity')

import InsertionSort
space_complexity(InsertionSort.insertion_sort)
