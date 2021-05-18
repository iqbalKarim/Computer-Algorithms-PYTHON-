import numpy as np
import random

def SelectionSort(a):
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range (i+1, n):
            if a[j] < a[min]:
                min = j
            (a[i], a[min]) = (a[min], a[i])

###########################################

def BubbleSort(a):
    n = len(a)
    for i in range (n):
        for j in range (n-1-i):
            if a[j+1] < a[j]:
                (a[j+1], a[j]) = (a[j], a[j+1])

###########################################

def BubbleSort_while(a):
    exchange = True
    i = 0
    n = len (a)
    while i < n-2 and exchange:
        exchange = False
        for j in range (n-1-i):
            if a[j+1] < a[j]:
                (a[j+1], a[j]) = (a[j], a[j+1])
                exchange = True

###########################################

def Merge(a,b,c):
    i = j = k = 0
    p = len(b)
    q = len(c)
    
    while i < p and j < q:
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1
    if i == p:
        a[k:] = c[j:]
    else:
        a[k:] = b[i:]
            

def MergeSort(a):
    n = len (a)
    if n > 1:
        mid = n//2
        b = a[:mid]
        c = a[mid:]
        MergeSort(b)
        MergeSort(c)
        Merge(a,b,c)

###########################################

def InsertionSort(a):
    n = len (a)
    for i in range (n):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a [j+1] = a[j]
            j = j - 1
        a[j + 1] = v

###########################################

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
        
def QuickSort(a, l, r):
    if l < r:
        s = HoarePartition(a, l, r)
        QuickSort(a, l, s-1)
        QuickSort(a, s+1, r)
        
    



a = []
for i in range (20):
    a.append(random.randint(1,50))
print (a)
QuickSort(a, 0, len(a)-1)
print (a)

