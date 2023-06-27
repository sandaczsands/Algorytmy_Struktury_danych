import time, random, numpy as np

import random,time, sys
sys.setrecursionlimit(200000000)

f=open("operacje.txt","a")
operacje=0


def bublesort(t):
    global operacje
    for i in range(len(t)):
    #for dla nieposortowanych elementow
        for j in range(0,len(t)-1-i):
        #porownywanie sasiadow
        #print(t[j])
        #print(t[j+1])
            operacje+=1
            if t[j]>t[j+1]:
                t[j],t[j+1]=t[j+1],t[j]
                operacje+=1
          
def selectionSort(dane):
    global operacje
    n=len(dane)
    for j in range(0,n-1):
        minimum=j
        for i in range(j+1,n):
            operacje+=1
            if dane[i] < dane[minimum]:
                minimum = i
        dane[minimum],dane[j] = dane[j],dane[minimum]
        operacje+=1

    
def insertionsort(t):
    global operacje
    for i in range(1,len(t)):
        j=i
        while t[j-1]>t[j] and j>0:
            operacje+=1
            t[j-1],t[j]=t[j],t[j-1]
            j-=1
        operacje+=1


def mergeSort(arr):
        global operacje
        if len(arr) > 1:
            mid = len(arr)//2
            sub_array1 = arr[:mid]
            sub_array2 = arr[mid:]
            mergeSort(sub_array1)
            mergeSort(sub_array2)
            i = j = k = 0
            while i < len(sub_array1) and j < len(sub_array2):
                operacje+=1
                if sub_array1[i] < sub_array2[j]:
                    arr[k] = sub_array1[i]
                    i += 1
                else:
                    arr[k] = sub_array2[j]
                    j += 1
                k += 1
        
            while i < len(sub_array1):
                arr[k] = sub_array1[i]
                i += 1
                k += 1
            while j < len(sub_array2):
                arr[k] = sub_array2[j]
                j += 1
                k += 1
        


def heapify(dane,n,i):
    global operacje
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    operacje+=1
    if (l < n) and (dane[i] < dane[l]):
        largest = l
    operacje+=1
    if (r < n) and (dane[largest] < dane[r]):
        largest = r
    #szukamy najwiekszej wartosci
    if largest != i:
        operacje+=1
        dane[i], dane[largest] = dane[largest], dane[i]
        heapify(dane,n,largest)

def heapSort(dane):
    global operacje
    n = len(dane)
    for i in range(n//2,-1,-1):
        heapify(dane,n,i)
    for i in range(n-1,0,-1):
        operacje+=1
        dane[i],dane[0]=dane[0],dane[i]
        heapify(dane,i,0)



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return np.concatenate((quicksort(smaller), equal, quicksort(larger)))
a = []
b = []
c = []
d = []
e = []
n=50000

for j in range (2000,20001,2000):
    n=0
    n=n+j
    for i in range(0,n):
        a.append(i)

    for i in range(0,n):
        b.append(i)
    b=b[::-1]

    for i in range(n):
        c.append(random.randint(1,999999))
    
    def ShapeV(n):
        t=[]
        for i in range(0,n//2):
            t.append(i)
        t=t[::-1]+t
        return t

    def ShapeA(n):
        t=[]
        for i in range(0,n//2):
            t.append(i)
        t=t+t[::-1]
        return t

    tab=[a,b,c,ShapeV(n),ShapeA(n)]
    #bubble+
    #selection+
    #insertion+
    #quick
    #heap+
    #merge+

    print("ilosc elementow to: ",n)


    for i in tab:
        start=time.time()
        quicksort(i)
        i=i[::-1]
        end=time.time()
        print(end-start)
        f.write(str(operacje)+"\n")
        #print("ilosc operacji ;", operacje)
        operacje=0
    f.write("\n")


f.close()


