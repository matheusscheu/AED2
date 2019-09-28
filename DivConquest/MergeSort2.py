def MergeSort(array,init,end):
    if init < end:
        mid = (init+len(end)//2)
        MergeSort(array,init,mid)
        MergeSort(array,mid,end)
        Merge(array,init,mid,end)

def Merge(array,init,mid,end):
    n1 = meio - init
    n2 = end - meio 

    l = n1*[None]
    r = n2*[None]
    i = j = 0

    for k in range(init,end):
        if l[i] <= r[j]:
            array[k]= l[i] 
            i+=1
        else:
            array[k] = r[j]
            j+=1

print(MergeSort([3,2,1],0,3))

