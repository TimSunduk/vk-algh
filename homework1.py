#this file includes all task from 1st seminar and its homework,on theme "Massives"

# in all tasks I tried to make them O(1)/O(n) without extra allocations ( Memo O(~1-n) )
import random
import math

def swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr
def randomArray(arr):
    for i in range(0, random.randint(3,6)):
        arr.append(random.randint(0,4))
    return arr
def reverseArray(arr,left,right):
    while ( left < right ):   #till mid
        arr[left], arr[right] = arr[right], arr[left]  #swap elements
        left += 1
        right -= 1


    return arr

def reversePartArray(arr, k):
    n = len(arr)
    reverseArray(arr, 0 , n - 1 )
    reverseArray(arr, 0 , k % n  - 1 )
    reverseArray(arr, k % n  , n - 1 )
    return 0

def mergeSortArrayMemo(arr1, arr2 ):
    merged_arr = []
    i = 0
    j = 0

    while ( i < len(arr1) and j < len(arr2)):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    if i < len(arr1)-1: merged_arr.append(arr1[i:])
    if j < len(arr2)-1 : merged_arr.append(arr2[j:])

    return merged_arr

def mergeSortArray(arr1, arr2 ):

    for i in range(len(arr2)): arr1.append(0)

    pointer1= len(arr1) - len(arr2) - 1
    pointer2= len(arr2)-1
    pointer3=  len(arr1)-1

    while pointer2 >=0 :
        if (pointer1 >=0) and (arr1[pointer1] > arr2[pointer2]):
            arr1[pointer3] = arr1[pointer1]
            pointer1 -= 1

        else:
            arr1[pointer3] = arr2[pointer2]
            pointer2 -= 1

        pointer3 -= 1
    return arr1


def evenFirst(arr):
    i, eveni = 0, 0
    for i in range (len(arr)):
        if arr[i] % 2 == 0:
            swap(arr,i,eveni)
            eveni += 1

    return arr

def nullLast(arr):
    nuli = len(arr) - 1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0:
            swap(arr,i,nuli)
            nuli -= 1
    return arr

def nullLastSort(arr):
    nuli = 0
    i = 0
    while nuli < len(arr) and i < len(arr):

        if arr[i]==0:
            swap(arr,nuli, i)
            nuli += 1
        else:
            i += 1
            nuli = i
    print(i,'\n',nuli)

    return arr


# initA =  list(map(int, input('Введите исходный массив ').split()))       # считка частей строк, разделенных пробелом, переведенных в целое число ( чтобы задать любой массив )

exitCheck = -1
initA = []
initB = []
print('Какую функцию выполнить?')

while ( exitCheck != 0 ):
    whatDo = input()
    match whatDo:
        case 'nullLast':
            print(nullLastSort(initA))

        case 'evenFirst':
            print(evenFirst(initA))

        case 'rands':
            initA, initB = [], []
            randomArray(initB)
            randomArray((initA))

            print('array A: ', initA, '\narrayB: ', initB)

        case 'mergememo':
            print('array A: ',initA,'\narrayB: ', initB)
            print(mergeSortArrayMemo(initA,initB))

        case 'merge':
            print('array A: ', initA, '\narrayB: ', initB)
            print(mergeSortArray(initA, initB))

        case 'sorts':
            initA.sort()
            initB.sort()
            print('array A: ',initA,'\narrayB: ', initB)

        case 'clears':
            initA = []
            initB = []
            print(initA)

        case 'randa':
            randomArray(initA)
            print(initA)

        case 'showa':
            print(initA)

        case 'seta':
            initA = []
            initA = list(map(int, input('Введите исходный массив ').split()))
        case 'sets':
            initA = list(map(int, input('Введите исходный массив A ').split()))
            initB = list(map(int, input('Введите исходный массив B ').split()))
        case 'rpa':
            temp = int(input('set which part '))
            if temp == 0:
                reverseArray(initA, 0, len(initA)-1 )
                print('ra done ')
            else:
                reversePartArray(initA, int(temp) )
                print('rpa done ')
            print(initA)

        case '0':
            exitCheck = 0




