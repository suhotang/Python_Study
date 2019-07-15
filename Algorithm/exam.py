## k번째 수
def solution(arr, com):
    ans = []
    for i in com:
        a= arr[i[0]-1:i[1]]
        a.sort()
        ans.append(a[i[2]-1])
    return ans


arr = [1,5,2,6,3,7,4]
com=[[2,5,3],[4,4,1],[1,7,3]]
print(solution(arr,com))
