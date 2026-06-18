# Rock Paper Scissor
# user1 user2 
# same same  = Match Tie!
# rock paper = user2 winner 
# rock scissor = user1 winner
# paper scissor = user2 winner 
# paper rock = user1 winner 
# scissor paper = user1 winner 
# scissor rock = user2 winner 

options = {"1":"rock","2":"paper", "3":"scissor"}

while True:
    user1 = input("User1 Select One Item: \n\t1.Rock \n\t2.Paper \n\t3.Scissor \n\t :  ")
    user2 = input("User2 Select One Item: \n\t1.Rock \n\t2.Paper \n\t3.Scissor \n\t :  ")
    print("--"*20)
    print(f"\n{user1=} {user2=}")

    user1 = user1.lower()
    user2 = user2.lower()
    if user1 not in options or user2 not in options:
        print("Invalid Selection by user \n\t {user1=} {user2=}")
    elif user1 == user2:
        print("Match Tie!")
    elif ((user1 == "rock" and user2 == "paper") or 
        (user1 == "paper" and user2 == "scissor") or 
        (user1 == "scissor" and user2 == "rock")):
        print("\n\n\t" , "****** USER 2 Wins  ****","\n\n\t")
    else:
        print("\n\n\t" , "****** USER 1 Wins  ****","\n\n\t")
    
    play = input("Enter 'q' to quit or any key to play one more game : ")
    if play == "q":
        break
    print("---"*25)


# options - dictionary 
# valid user1/user2 in option.keys() or options.values()
# write a function to take the input 
# write a function for winner message
############# Mutiple games #########
# get the count 4
# winner will be who wins more games
# If any user wins 60% of games continously declare that user as Winner 
