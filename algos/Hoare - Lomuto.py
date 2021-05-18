def HoarePartition(a, l, r):
    p = a[l]
    i = l
    j = r

    while i < j:
        while i <= j and a[i] <= p:
            i += 1
        while i <= j and a[j] >= p:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]

    if a[l] > a[j]: 
        a[l] , a[j] = a[j], a[l]
    return j


#####################################

def LomutoPartition(a):
    p = a[0]
    s = 0
    l = 0
    r = len(a)-1
    
    for i in range(l+1, r):
        if a[i] < p:
            s += 1
            a[s], a[i] = a[i], a[s]
    a[l], a[s] = a[s], a[l]
    return s




a = [10,7,8,9,1,5]

LomutoPartition(a)
print (a)
