def timecomplexity(fn):
    import timeit
    import random
    import GraphicalAnalysis
    Input_X = []
    Time_per_input_Y = []
    #z=[2**i for i in range(1,16)]
    for i in range(2,101,2):
        N_input=[]
        for j in range(i):
            N_input.append(random.randint(1,100000))
        s = fn +'('+str(N_input)+')'
        Input_X.append(i)
        Time_per_input_Y.append(timeit.timeit(stmt=s,globals=globals(),number=1000))#Multiplying seconds with 1000 = ms
    GraphicalAnalysis.singlegraph(Input_X,Time_per_input_Y,y_label='Time-->ms',title='Time Complexity')

#import InsertionSort
#timecomplexity('InsertionSort.insertion_sort')

import MergeSort
timecomplexity('MergeSort.mergesort')
