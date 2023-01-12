def task(num):
    c=0
    for i in range(1,num+1):
        if(num%i==0):
            c+=1
    if c==2:
        print(num)
l=[1,2,4,5,7,8,12,11]
result=list(map(task,l))