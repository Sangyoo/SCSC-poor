print'Input range(1 - 5000) : '
count=raw_input()
number=1
Time=0
Ten=10
while int(count)!=0:
    A=number/Ten%10
    if number<10:
        A=number%10
            if A%3==0:
                Time=Time+1
            else:
                Time=Time+0
                
    if A%3==0:
        Time=Time+1
        else:
            Time=Time+0
    if A<0:
        time=time+0
    print'Clap'*Time

    count=count-1
    number=number+1

�ڸ��� ����

number=raw_input()
count=0
def digit(A):
    while A!=0:
        A=A/10
        count=count+1
    return count

digit()��� �Լ��� ������ �ڸ����� ����

n���ڸ��� ���� n��° + n-1��° ...1��° ���ڱ��� 3�� ��ִ��� ������.

n�� �ڸ� ���ϴ� �� = number/10��(n-1)��%10
ten=10
n=digit(number)
while n!=1:
    ten=ten^n
    if number/ten%10%3==0:
        time=time+1
    else:
        time=time+0
    n=n-1
    number=number+1
