import random
n=int(input("ENTER NUMBER OF ROUNDS:"))
for i in range(n):
    user_choice=int(input("ENTER YOUR CHOICE: 0 for ROCK ,1 for PAPER , 2 for SCISSORS\n"))
    computer_choice=random.randint(0,2)
    a=['ROCK',' PAPER',' SCISSORS']
    print("YOU CHOSE:",a[user_choice])
    print("COMPUTER CHOSE:",a[computer_choice])
    if(computer_choice==user_choice):
        print("DRAW")
    elif(user_choice==0 and computer_choice==2):
        print("YOU WIN")     
    elif(computer_choice>user_choice):
        print("YOU LOOSE")    
    elif(user_choice>computer_choice):
        print("YOU WIN")   
    elif(computer_choice==0 and user_choice==2):
        print("YOU LOOSE")  
          