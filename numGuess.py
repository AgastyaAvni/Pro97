intro=input('Welcome To num guess !!! Guess a num between 10 and you win you have 5 chances')
chances=5
cAns=7

for i in intro:
    chances=chances-1
    if(i==7):
        print('You Win')

if(chances==0):
    print('You Lose')    
