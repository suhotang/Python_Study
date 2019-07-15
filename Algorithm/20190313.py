# 피보나치 수열
def solution(x):
    if x<2:
        return x
    else :
        return solution(x-1)+solution(x-2)

#print(solution(6))

# 조합의 수를 계산하는 경우
# n개의 서로 다른 원소에서 m개를 택하는 경우의 수

from math import factorial as f

def combi(n,m):
    return f(n) / (f(m)*f(n-m))

#print(combi(10,3))

# 재귀로 구현

def combi_j(n,m):
    if n==m:
        return 1
    elif m==0:
        return 0
    else:
        return combi_j(n-1,m)+combi_j(n-1,m-1)

# 하노이 탑
# x는 원판의 개수
def hanoi(x):
    if x==1:
        return x
    else :
        return

# 재귀 이진탐색

list=[2,4,6,10,14,20]
def binsearch(L,x,l,u):
    if l > u:
        print("lower : ",l)
        print("upper : ",u)
        return -1
    mid=(l+u)//2
    if x == L[mid]:
        return mid
    elif x<L[mid]:
        print("upper : ",u)
        return binsearch(L,x,l,mid-1)
    else:
        print("lower : ",l)
        return binsearch(L,x,mid+1,u)

print(binsearch(list,3,0,len(list)-1))
