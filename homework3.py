import random
import math


def swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr
def randomArray(arr):
    for i in range(0, random.randint(4,9)):
        arr.append(random.randint(1,9))
    return arr

def recbinser(arr, l, r, target):
    if l > r:
        return -1

    middle = int((l+r)/2)

    if arr[middle] == target:
        return middle

    if arr[middle] > target:
        return recbinser(arr, l , middle -1 , target )
    else:
        return recbinser(arr, middle+1, r, target )

def itbinser(arr, target):
    l = 0
    r = len(arr) -1

    if target < arr[0] or target > arr[r]:
        return -1

    while l <= r:
        middle = int((l+r)/2)
        if target == arr[middle]:
            return middle

        if target < arr[middle]:
            r = middle - 1
        else:
            l = middle + 1

    return -1


def lefbinser(arr, target):
    l = 0
    r = len(arr)-1
    while (l+1) < r:
        middle = int( (l+r)/2 )
        if arr[middle]<target:
            l = middle
        else:
            r = middle


    if arr[l] == target:
        return l
    if arr[r] == target:
        return r
    return -1

def rigbinser(arr, target):
    l = 0
    r = len(arr) - 1
    while (l + 1) < r:
        middle = int((l + r) / 2)
        if arr[middle] <= target:
            l = middle
        else:
            r = middle

    if arr[r] == target:
        return r
    if arr[l] == target:
        return l
    return -1


def ansbinser(w, h, n):
    l = max(w,h)
    r = l * n
    while l + 1 < r:
        middle =  ( (r+l)//2 )
        res = (middle//w) * (middle//h)
        if res < n:
            l = middle
        else:
            r = middle
    return r

def recterser(arr, l, r, target):
    if ( r >= l ):
        m1 = l + ( r- l )//3
        m2 = r - ( r - l)//3

        if arr[m1] == target:
            return m1
        if arr[m2] == target:
            return m2


        if target < arr[m1]:
            return recterser(arr,l, m1 -1 , target)
        elif target > arr[m2]:
            return recterser(arr, m2+1, r, target)
        else:
            return recterser(arr, m1+1, m2-1, target)

    return -1

def itterser(arr, target):
    l = 0
    r = len(arr)-1
    while( r>= l ):

        m1 = l + (r-l)//3
        m2 = r - (r-l)//3

        if arr[m1] == target:
            return m1
        if arr[m2] == target:
            return m2
        if target < arr[m1]:
            r = m1-1
        elif target > arr[m2]:
            l = m2+1
        else:
            l = m1+1
            r = m2-1
    return -1


def exposer( arr, target):
    border = 1
    lastel = len(arr)-1
    while border<lastel and arr[border]<target:
        border = border * 2
        if arr[border] == target:
            return border
        if border > lastel:
            border = lastel

    return recbinser(arr, border//2, border, target)


def interpolser(arr, needle):
    return -1 ### STILL TO DO!!!!!!!!!!!!!!

# tasks

def copyTime(n,x,y):
    l = 0
    r = (n-1)*max(x,y)
    while l+1<r:
        mid = (r+l)//2
        if mid//x + mid//y < n-1:
            l = mid
        else:
            r = mid

    return r + min(x,y)

def issubseq(a,b):
    q = queue()  ### CREATE DEF QUEUE()!!!!!!!!
    for el in a:
        q.push(el)

    for el in b:
        if q.peek() == el:
            q.pop()

    return q.getSize() == 0


def issubseq1(a,b):
    pa = 0
    pb = 0
    while pa < len(a): #len a as big
        if a[pa] == b[pb]:
            pb += 1
        if pb == len(b): # len b as small
            return True
        pa += 1

    return False

def deldup(str):







# initA =  list(map(int, input('Введите исходный массив ').split()))       # считка частей строк, разделенных пробелом, переведенных в целое число ( чтобы задать любой массив )

exitCheck = -1
initA = []
initB = []
print('Какую функцию выполнить?')

while ( exitCheck != 0 ):
    whatDo = input()
    match whatDo:
        case 'issubseq1':
            print(issubseq1(input(),input()))
        case 'issubseq':
            print(issubseq((input()), (input())))


        case 'copytime':
            n,x,y = map(int, input('set n, x, y ').split())
            print(copyTime(n,x,y))
        case 'exposer':
            print(exposer(initA, int(input())))

        case 'recterser':
            l, r, target = map(int, input('set left, right, target ').split())
            print(recterser(initA, l, r, target))

        case 'itterser':
            print(itterser(initA, int(input())))

        case 'ansbinser':
            w,h,n = map(int, input('set w,h,n ').split())
            print(ansbinser(w,h,n))
        case 'lefbinser':

            print(lefbinser(initA, int(input())))
        case 'rigbinser':

            print(rigbinser(initA, int(input())))

        case 'itbinser':
            target = int(input())
            print(itbinser(initA, target))

        case 'recbinser':
            l,r,target = map( int, input('set left, right, target ').split())
            print(recbinser(initA,l,r,target))
        case 'rands':
            initA, initB = [], []
            randomArray(initB)
            randomArray((initA))

            print('array A: ', initA, '\narrayB: ', initB)


        case 'sorts':
            initA.sort()
            initB.sort()
            print('array A: ',initA,'\n n: ', len(initA))

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

        case '0':
            exitCheck = 0
