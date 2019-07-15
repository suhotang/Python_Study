num, room_max = input().split()

list_girl=[0,0,0,0,0,0]
list_boy=[0,0,0,0,0,0]

for i in range(int(num)):
        a, b = input().split()
        a=int(a)
        b=int(b)
        if a==1:
            list_boy[b-1]=list_boy[b-1]+1
        else :
            list_girl[b-1]=list_girl[b-1]+1
count=0

room_max=int(room_max)

for i in list_girl:
    if (i%room_max)==0:
        count=count+(i//room_max)
    else:
        count=count+(i//room_max)+1

for i in list_boy:
    if (i%room_max)==0:
        count=count+(i//room_max)
    else:
        count=count+(i//room_max)+1

print(list_girl)
print(list_boy)
print(count)





