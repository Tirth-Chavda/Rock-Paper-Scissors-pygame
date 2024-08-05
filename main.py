import random

def list1():
    return  ["Rock" , "Paper" , "Scissors"]
    
def computer():
    choice = list1()
    comp = random.choice(choice)
    print(f"Computer's choice is : {comp}")
    return comp

def player():
    print("Press 1 for Rock")
    print("Press 2 for Paper")
    print("Press 3 for Scissors")
    player_choice = int(input("Select your choice : "))
    if player_choice==1:
        print("Player's Choice is : Rock")
    elif player_choice==2:
        print("Player's Choice is : Paper")
    elif player_choice==3:
        print("Player's Choice is : Scissors")
    else:
        print("Invalid Input")
    return player_choice
    
def game():
    player_choice = player()
    comp_choice = computer()
    if player_choice==1 and comp_choice=="Rock":
        print("DRAW")
    elif player_choice==1 and comp_choice=="Paper":
        print("Computer WIN")
    elif player_choice==1 and comp_choice=="Scissors":
        print("Player WIN")
    elif player_choice==2 and comp_choice=="Rock":
        print("Player WIN")
    elif player_choice==2 and comp_choice=="Paper":
        print("DRAW")
    elif player_choice==2 and comp_choice=="Scissors":
        print("Computer WIN")
    elif player_choice==3 and comp_choice=="Rock":
        print("Computer WIN")
    elif player_choice==3 and comp_choice=="Paper":
        print("Player WIN")
    elif player_choice==3 and comp_choice=="Scissors":
        print("DRAW")
    else:
        pass

def main():
    print("____________Welcome in Rock-Paper-Scissors Game____________")
    game()
    
if __name__ == "__main__":
    main()