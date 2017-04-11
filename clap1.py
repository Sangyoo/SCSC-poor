#2017/03/22
# 369°ÔÀÓ

print'Input range(1 - 5000) : '
count=raw_input()
number=1
time=0
1548


n=2
Ten=10
while n!=0:
    A=number/Ten%10
    if number<10:
        A=number%10
            if A%3==0:
                Time=Time+1
    if A<0:
        break
    else:
        if A%3==0:
                Time=Time+1
    if number/Ten%10<0:
        break
count=count+1
Ten=Ten*10
number=number+1

while int(count)!=0:
    if number<10:
        if int(number)%3==0:
            print'Clap!'
        else:
            print number

    if number/10>0:
        div=number/10
        if div%3==0 and number/10%3==0:
            print'Clap!clap!'
        if div%3==0 and number/10%3!=0:
            print'Clap!'
        else:
            print number

    if number/100>0:
        A=number%10 
        B=number/10%10 
        C=number/100%10

        if A%3==0:
            time=time+1
        else:
            time=time+0
        if B%3==0:
            time=time+1
        else:
            time=time+0
        if C%3==0:
            time=time+1
        else:
            time=time+0

        print'Clap!'*time
    count=int(count)-1
    number=number+1
