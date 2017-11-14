import sys

def solveMeFirst(a,b):
    return a+b


def simpleArraySum(n, ar):
    res = 0
    for i in ar:
        res += i
    return res


def aVeryBigSum(n, ar):
    summ = 0
    for a in ar:
        summ += a
    return summ
    # Complete this function

def diagDifference():
    n = int(raw_input().strip())
    a = []
    for a_i in xrange(n):
        a_temp = map(int,raw_input().strip().split(' '))
        a.append(a_temp)
    diagA = 0
    diagB = 0
    pos = 0
    for row in a:
        diagA += row[pos]
        diagB += row[len(row) - 1 - pos]
        pos +=1
    print abs(diagA - diagB)

def plusMinus():
    n = int(raw_input().strip())
    arr = map(int,raw_input().strip().split(' '))
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos+=1
        elif i < 0:
            neg +=1
        else:
            zero+=1
    print pos * 1.0 / len(arr)
    print neg * 1.0 / len(arr)
    print zero * 1.0 / len(arr)

def stairCase(n):
    rowNum = 1
    for row in range(n):
        print (n-rowNum)* " " + (rowNum)*"#"
        rowNum+=1

def minmaxSum():
    arr = map(int, raw_input().strip().split(' '))
    arr =  sorted(arr)
    print sum(arr) - arr[4], sum(arr) - arr[0]


def birthdayCakeCandles(n, ar):
    candle = max(ar)
    count = ar.count(candle)
    return count
    # Complete this function

def timeConversion(s):
    status = s[-2:]
    if status == "AM":
        if s[:2] == "12":
            return "00" + s[2:-2]
        return s[:-2]
    else:
        if s[:2] == "12":
            return s[0:-2]
        newHour = str(int(s[:2]) + 12)
        return newHour + s[2:-2]
    # Complete this function
