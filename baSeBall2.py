#100자리가 0은 아님
#중복숙자는 x
#다만들면 자릿수 받아서 게임하기
#그것도 다하면 컴퓨터끼리 하기
#2015016535 이상유
import random

def getSecretNumber():#랜덤한 숫자 하나 만들기
    a=random.randint(1,9)
    b=random.randint(0,9)
    while a==b:
        b=random.randint(0,9)
    c=random.randint(0,9)
    while a==c or b==c:
        c=random.randint(0,9)

    return 100*a+10*b+c

def getNumber(alreadyGuessed):#function:들어온 숫자 판단
    numList='123456789'.split()
    Already=0
    while True:
        print 'Guess a number (3-digit)'
        guess=raw_input()
        
        if guess in alreadyGuessed:#이미 입력한숫자인 경우
            print ' You have already guesses that number. Choose again. '
            
        elif len(guess)!=3 and (guess)/100!=0:#3자리수가 아닌 경우
            print ' Please enter a three-digit number. '

        
        elif guess[0]==guess[1] or guess[2]==guess[0] or guess[1]==guess[2]:
             print ' Your number has duplicated elements! Choose again. '
                
        else:
            return guess

def checkBall(guess):
    #ball 판단
    ball=0
    for i in range(len(guess)):
        if guess[i] in str(secretNumber):
            ball=ball+1
            if guess[i] in str(secretNumber)[i]:
                ball=ball-1
         
    return ball


def checkStrike(guess):
    #strike 판단
    strike=0
    for i in range(len(guess)):
        if guess[i] in str(secretNumber)[i]:
            strike=strike+1
    return strike

def displayBoard():
    print' Number Baseball(No jam) '
    print ' Start'

def playAgain():
    print 'Do you want to play agian? (yes or no)'
    return raw_input().lower().startswith('y')


secretNumber=getSecretNumber()
print secretNumber
ball=0
strike=0
gameIsDone=False
alreadyGuessed=' '
displayBoard()
while True:
    guess=getNumber(alreadyGuessed)
    alreadyGuessed=alreadyGuessed+guess
    print str(guess),
    if checkBall(guess)==0 and checkStrike(guess)==0:
        print '---- Out! Idiot! '
    elif checkBall(guess)==0 and checkStrike(guess)!=0 and checkStrike(guess)!=3:
        print ' ---- '+str(checkStrike(guess))+' strike'
    elif checkStrike(guess)==0:
        print ' ---- '+str(checkBall(guess))+'ball'
    elif checkStrike(guess)==3:
        print '---- Homerun! Good job '
        gameIsDone=True
    else:
        print ' ---- '+str(checkBall(guess))+' ball' + str(checkStrike(guess))+' strike'
        

    if gameIsDone:
        if playAgain():
            secretNumber=getSecretNumber()
            ball=0
            strike=0
            gameIsDone=False
            alreadyGuessed=' '
        else:
            break
            
        
        
    


#get number


