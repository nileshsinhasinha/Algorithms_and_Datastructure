"""Heap is a data structure which is almost complete tree (Either binary or ternary)
For Min heap  implementation we can directly use heapq library of python
Here, we will be implementing Max Heap implementation"""

def max_heapify(Arr,node):
    """It will heapify the tree or subtree of which node will be provided"""
    #[1,5,6,8,12,14,16]
    #Indices of array is starting from 0
    left_node,right_node=2*node+1,2*node+2
    #To find the largest between parent node and left node
    if (left_node <= len(Arr)-1) and (Arr[left_node]>Arr[node]):
        largest= left_node
    else:
        largest=node
    #To find out the largest between largest node determined above and right node
    if (right_node <= len(Arr)-1) and (Arr[right_node]>Arr[largest]):
        largest= right_node
    #Swapping between the largest and parent node and calling
    #max_hapify again to determine the changes in below subtrees
    if largest != node:
        Arr[node],Arr[largest]=Arr[largest],Arr[node]
        max_heapify(Arr,largest)
    #return Arr


def build_max_heap(Arr):
    heap_size=(len(Arr)-1)//2
    for i in range(heap_size,-1,-1):
        max_heapify(Arr,i)

def delete_max_heap_value(Arr):
    """To delete maximum value from max heap with keeping intact heap property"""
    if len(Arr)<2:
        raise ValueError('Head underflow')

    max,Arr[0] = Arr[0],Arr[len(Arr)-1]
    Arr.pop()
    max_heapify(Arr,0)
    return max

def increase_heap_node_value(Arr,node,value):
    import math
    """To update the value of a node to the higher value"""
    if value<Arr[node]:
        raise ValueError("Value entered is lower than the present index value")

    Arr[node]=value
    #print(Arr)
    while (node>0) and (Arr[math.ceil(node/2)-1]<Arr[node]):
        Arr[math.ceil(node/2)-1],Arr[node]=Arr[node],Arr[math.ceil(node/2)-1]
        node=math.ceil(node/2)-1

def insert_heap_node(Arr,value):
    import math
    """To insert the new node"""
    new_node=len(Arr)
    Arr.append(value)
    #print(Arr)
    while (new_node>0) and (Arr[math.ceil(new_node/2)-1]<Arr[new_node]):
        Arr[math.ceil(new_node/2)-1],Arr[new_node]=Arr[new_node],Arr[math.ceil(new_node/2)-1]
        new_node=math.ceil(new_node/2)-1

l=[100,99,88,98,97,79,92,96,95,94,93,49,48,39,38]
#max_heapify(l,0)
build_max_heap(l)
# print(l)
# #print(delete_max_heap_value(l))
# #increase_heap_node_value(l,5,100)
# insert_heap_node(l,35)
print(l)
