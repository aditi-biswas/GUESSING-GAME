import random as r

c=r.randint(1,100)
n=1
mylist=[]
d=[]

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

while True:
    guess=int(input('I\'m thinking of a number between 1 and 100.\n  What is your guess? '))
    if(guess<1 or guess>100):
        print("OUT OF BOUNDS ! Please try again: ")
    elif(guess==c):
        if(n==1):
            print("HURRAY!!!! \nYOU HAVE GUESSED IN ONLY 1 GUESS")
        else:
            print("HURRAY!!!! \nYOU HAVE GUESSED IN ONLY {} GUESSES".format(n))
        break
    elif(n==1):
        lst1=[x for x in range(c-10,c,1)]
        lst2=[x for x in range(c+1,c+11,1)]
        mylist=lst1+lst2
        if guess in mylist:
            print("WARM!")
        else:
            print("COLD!")
    else:
        if(c>guess):
            d.append(c-guess)
        else:
            d.append(guess-c)
        if(d[len(d)-1]<d[len(d)-2]):
            print("WARMER!")
        else:
            print("COLDER!")
    n+=1

