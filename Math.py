def smallestEven(n):
    return n if n%2==0 else 2*n

n=5
n=6
print(smallestEven(n))


def noOfCommonFactors(a,b):
    return [i for i in range(1,min(a,b)+1) if a%i==0 and b%i==0]

a = 12
b = 6
a = 25
b = 30
print(noOfCommonFactors(a,b))


def tempConversion(c):
    return [c+273.15,c*1.8+32.00]

print(tempConversion(36.50))


def sumof(n):
    s={}
    while len(str(n))!=1:
        n=sum([int(i) for i in str(n)])
    return n

print(sumof(38))


def sumOfDigit(s,k):
    res=""
    for i in s:
        res=res+str(ord(i)-96)
    for i in range(k):
        res=sum([int(i) for i in str(int(res))])
    return res

s="iiii"
k=1
s="leetcode"
k=2
s="zbax"
k=2
print(sumOfDigit(s,k))


def findIfDigitGame(arr):
    s=[i for i in arr if i/10<1]
    d=[i for i in arr if i/10>=1]
    if sum(s)==sum(d):
        return False
    return True

a=[1, 2, 3, 4, 5, 14]
a=[1,2,3,4,10]
print(findIfDigitGame(a))


def findNumWithEven(a):
    res=[str(i) for i in a]
    return len([i for i in res if len(i)%2==0])

a=[12,345,2,6,7896]
print(findNumWithEven(a))


def countTheDigits(n):
    c=0
    for i in str(n):
        if n%int(i)==0:
            c+=1
    return c

n=1248
n=121
print(countTheDigits(n))

