def greatestEngAndLow(s):
    u = set([i for i in s if i.isupper()])
    l = set([i for i in s if i.islower()])
    res=[i for i in u if i.lower() in l]
    if res==[]:
        return ""
    else:
        return sorted(res)[-1]

a = "arRAzFif"
a="lEeTcOdE"
a="AbCdEfGhIjK"
print(greatestEngAndLow(a))


def defangingIp(s):
    return s.replace(".","[.]")

a="1.1.1.1"
a="255.100.50.0"
print(defangingIp(a))


def reversePrefix(a,ch):
    if ch not in a:
        return a
    else:
        return a[:a.index(ch)+1][::-1]+a[a.index(ch)+1:]

a="abcdefd"
ch='d'
a="xyxzxe"
ch='z'
print(reversePrefix(a,ch))


def truncateSentence(s,k):
    res=s.split(" ")
    if len(res)<k:
        return " ".join(res)
    else:
        return " ".join(res[:k])

s = "Hello how are you Contestant"
k=4
print(truncateSentence(s,k))


def stringArrayEquivalent(w1,w2):
    return "".join(w1)=="".join(w2)

a=["abc", "d", "defg"]
b=["abcddefg"]
a=["a", "cb"]
b=["ab", "c"]
print(stringArrayEquivalent(a,b))


def secondLargestDigit(s):
    res=sorted(set([i for i in list(s) if i.isdigit()]))
    if len(res)<2:
        return -1
    else:
        return int(res[-2])

s = "dfa12321afd"
print(secondLargestDigit(s))


def sortingSentence(a):
    li=a.split(" ")
    r=list(map(lambda x:x[-1]+x[:len(x)-1],li))
    r.sort()
    return list(map(lambda x:x[1:],r))

s = "is2 sentence4 This1 a3"
s = "Myself2 Me1 I4 and3"
print(sortingSentence(s))


def kthLargestInteger(a,k):
    return str(sorted([int(i) for i in a])[::-1][k-1])

a=["3", "7", "6", "10"]
k = 4
a=["2","21","12","1"]
k = 3
print(kthLargestInteger(a,k))


def numbersAreAscending(s):
    d=[int(i) for i in s.split(" ") if i.isdigit()]
    return d==sorted(set(d))

s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
s = "hello world 5 x 5"
s="sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
print(numbersAreAscending(s))


def firstPaliStr(arr):
    res=[i for i in arr if i==i[::-1]]
    if res==[]:
        return ""
    else:
        return res[0]

a=["abc","car","ada","racecar","cool"]
a=["notapalindrome","racecar"]
a=["def", "ghi"]
print(firstPaliStr(a))


def capitalizeTitle(s):
    l=s.split(" ")
    res=" ".join([i.title() if len(i)>2 else i.lower() for i in l])
    return res

s="First leTTeR of EACH Word"
s="i lOve leetcode"
s='l hV'
print(capitalizeTitle(s))


def divideAStrintoGroups(s,k,f):
    if len(s)%k!=0:
        s+=f*(k-(len(s)%k))
    return [s[i:i+k] for i in range(0,len(s),k)]

s = "abcdefghij"
# s = "abcdefghi"
k = 3
fill = "x"
print(divideAStrintoGroups(s,k,fill))


from collections import Counter
def largest3Same(s):
    l=list(s)
    c=Counter(l)
    res=sorted([k for k,v in c.items() if v>=3])
    pre=[i*3 for i in res if i*3 in s]
    if pre!=[]:
        return pre[-1]
    else:
        return ""

s="6777133339"
# s="2300019"
# s="42352338"
print(largest3Same(s))


def seniorCitizen(arr):
    res=list(map(lambda x:x[11:len(x)-2],arr))
    return len(list(filter(lambda x:int(x)>60,res)))

details = ["7868190130M7522",
           "5303914400F9211",
           "9273338290F4010"]
details = ["1313579440F2036","2921522980M5644"]
print(seniorCitizen(details))


def binaryDate(s):
    li=s.split("-")
    return "-".join(list(map(lambda x:bin(int(x))[2:],li)))

date = "2080-02-29"
date = "1900-01-01"
print(binaryDate(date))


def balancedString(s):
    li=list(num)
    e=[int(li[i]) for i in range(len(li)) if i%2==0]
    o=[int(li[i]) for i in range(len(li)) if i%2==1]
    return sum(e)==sum(o)

num = "1234"
num = "24123"
print(balancedString(num))