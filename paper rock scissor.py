import random
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(" % PAPER ROCK SCISSOR % ")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(" lets start the game!!......    ")
point=0
ai=0
hs=0
cs=0
ma=0
while(True):
    if(ma>5):
        print("$$$$$$$$$$$$$$$$$$$$$")
        print("total match:",ma)
        print("human score:",hs)
        print("AI score:",cs)
        if(hs>cs):
            print("congrats you won")
        elif(cs>hs):
            print("AI won......Better luck next time")
        else:
            print("MATCH DRAW")
        print("######################")
        break
    c=input(" choose paper->p   rock->r scissor->s   :   ")
    if(c=="p"):
        print("paper")
        point=10+random.randint(1,3)
        match point:
            case 11:
                ma=ma+1
                hs=hs+1
                print("Human:paper","AI:rock")
                print("Match: ",ma,"Human score:",hs,"AI score: ",cs)
                print("Human wins","AI lost")
                print("_________")
            case 12:
                ma=ma+1
                cs=cs+1
                
                print("Human:paper","AI:scissor")
                print("Match: ",ma,"Human score:",hs,"AI score: ",cs)
                print("Human lost","AI won")
                print("_________")
            case 13:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("Human:paper","AI:rock")
                print("Match: ",ma,"Human score:",hs,"AI score: ",cs)
                print("match draw")
                print("_________")
    elif(c=="r"):
        print("rock")
        point=20+random.randint(1,3)
        match point:
            case 21:
                ma=ma+1
                hs=hs+1
                print("Human:rock","AI:scissor")
                print("Match: ",ma,"Human score:",hs,"AI score: ",cs)
                print("Human wins","AI lost the match")
                print("_________")
            case 22:
                ma=ma+1
                cs=cs+1
                print("Human:rock","AI:paper")
                print("Match: ",ma,"Human score:",hs,"AI score: ",cs)
                print("Human lost","AI won the match")
                print("_________")
            case 23:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("Human:rock","AI:rock")
                print("Match: ",ma,"Human score:",hs,"AI score: ",cs)
                print("match draw")
                print("_________")
    elif(c=="s"):
        print("scissor")
        point=30+random.randint(1,3)
        match point:
            case 31:
                ma=ma+1
                hs=hs+1
                print("Human:scissor","AI:paper")
                print("Match: ",ma,"Human score:",hs,"AI score: ",cs)
                print("Human wins","AI lost the match")
                print("_________")
            case 32:
                ma=ma+1
                cs=cs+1
                print("Human:scissor","AI:rock")
                print("Match: ",ma,"Human score:",hs,"AI score: ",cs)
                print("Human lost","AI won the match")
                print("_________")
            case 33:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("Human:scissor","AI:scissor")
                print("Match: ",ma,"Human score:",hs,"AI score: ",cs)
                print("match draw")
                print("_________")