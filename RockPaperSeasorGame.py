import random

print("WELCOME")
choose =["r","p","s"]

usrpt=0
compt=0
chances=0

print("you have 10 Chances\nR=Rock\np=Paper\nS=Stone\nlets start")
while(chances<10):
    print("\nChoose(r,p,s) - ")
    userinput=input()
    randomchoice=random.choice(choose)

    if userinput==randomchoice:
        print(f"Computer Choosen - {randomchoice}")
        print(f"Both Choosen Same | No Points to both !\n Your Points = {usrpt} | Computer Points = {compt} ")

    elif userinput=="r" and randomchoice=="p" :
        compt=compt+1
        print(f"Computer Choosen - {randomchoice}")
        print(f"Computer Win !\n Your Points = {usrpt} | Computer Points = {compt} ")

    elif userinput=="p" and randomchoice=="s" :
        compt=compt+1
        print(f"Computer Choosen - {randomchoice}")
        print(f"Computer Win !\n Your Points = {usrpt} | Computer Points = {compt} ")

    elif userinput=="s" and randomchoice=="r" :
        compt=compt+1
        print(f"Computer Choosen - {randomchoice}")
        print(f"Computer Win !\n Your Points = {usrpt} | Computer Points = {compt} ")

    elif userinput=="p" and randomchoice=="r" :
        usrpt=usrpt+1
        print(f"Computer Choosen - {randomchoice}")
        print(f"You Win !\n Your Points = {usrpt} | Computer Points = {compt} ")

    elif userinput=="s" and randomchoice=="p" :
        usrpt=usrpt+1
        print(f"Computer Choosen - {randomchoice}")
        print(f"You Win !\n Your Points = {usrpt} | Computer Points = {compt} ")

    elif userinput=="r" and randomchoice=="s" :
        usrpt=usrpt+1
        print(f"Computer Choosen - {randomchoice}")
        print(f"You Win !\n Your Points = {usrpt} | Computer Points = {compt} ")

    else:
        print("Wrong Choice")

# chances not decreased if user inputed wrong choice hence used if

    if userinput =="r" or userinput=="p" or userinput=="s" :
        chances=chances+1
        print(f"Chances Left = {10-chances}")


print("\n.................Game Over...................")
if usrpt==compt:
    print("\nDraw ! *_*")
elif usrpt>compt:
    print(f"\nYour Points = {usrpt} | Computer Points = {compt} \n\n   YOU ARE THE WINNER (^^)")
elif compt>usrpt:
    print(f"\nYour Points = {usrpt} | Computer Points = {compt} \n\n  YOU LOOSE *_*")
