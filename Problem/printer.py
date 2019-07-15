#현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
#인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
#location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.

def solution(priorities, location):
    answer = 0
    fcount=0
    max_data=max(priorities)
    for i in priorities:
        if i==max_data:
            if location==0:
                answer=fcount
            priorities.pop(0)
            fcount+=1
            max_data=max(priorities)
        priorities.pop(0)
        priorities.append(i)
        location
    return answer
