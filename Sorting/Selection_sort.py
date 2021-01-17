def selectionsort(l):
    for i in range(len(l)):
        pos = i
        for j in range(i,len(l)):
            if l[j] < l[pos]:
                pos = j
        l[pos] , l[i] = l[i], l[pos]
    return l
