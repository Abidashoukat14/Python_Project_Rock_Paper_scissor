import random
computer=random.randint(0,2)
print("--------------------------------Welcome To the Game:---------------------------------\n")
print("--------------------------------Lets Start---------------------------------\n")
Rules=input("Do you know the rules of the game..?If Yes write 'yes' if No write 'no' :  ").lower()
if Rules=="yes":
  print("-------------------------------------------------------------------------------------------------------------------------\n")
  print("---------------------------------Okay! Thats cool.You are incredibal...Lets Start the game.------------------------------------------\n")
else:
    print("-------------------------------------------------------------------------------------------------------------------------\n")
    print("---------------Everthing is alright.Its your first time to Play this.So rules of game are shown below:-------------------------\n")
    print("=-----------------------------Rules of game are:------------------------------\n")
    print("                1) Rock break the Scissor.  And Rock is winner.  To select the Rock You have to choice 0 for Rock\n")
    print("                2) Paper cover the Rock. And Paper is winner.  To select the Paper You have to choice 1 for Paper\n")
    print("                3) Scissor cut the paper.And Scissor is winner.To select the Scissor You have to choice 2 for Scissor\n")
    print("------------------------Hope you understand the rules of game.--------------------------------\n")
    print("------------------------You are incredibal...Lets Start the game.--------------------------------\n")
  
while True:
                
                print("-------------------------------------------------------------------------------------------------------------------------\n")
                Player=int(input("                      Enter your Element.. '0' for Rock .'1' for Paper.And '2' for scissor.   "  ))
                quit=input(" \n         If you don't want to Play Feel free to quit the Game by enter 'quit' .If don't want to quit enter 'not quit': ").lower()
                try:
                        def check(computer,Player):
                               if computer<Player:
                                   return 1
                               elif computer>Player:
                                   return -1
                               else:
                                    return 0
                except ValueError as e:
                        print("Please Enter the valid Number for your Element")
        
                if Player>2 or Player<0 :
                      raise ValueError("Value should be 0 ,1 and 2")
                elif Player>=0 and Player<=2 and quit=="quit":
                       break
                elif Player<=0 or Player<=2 and quit=="not quit":
                     score=check(computer,Player)
                     if score==0:
                                        print(f" \n                                               This match is draw.                                       ")
                                        print(f"\n                              Computer choice the  {computer} and  you choice {Player}.                       ")
                                        print("\n-------------------------------------------------------------------------------------------------------------------------\n")

                     elif score==1:
                                        print(f"\n                                                  You Win this match.                                        ")
                                        print(f"\n                              Computer choice the  {computer} and  you choice {Player}.                       ")
                                        print("-------------------------------------------------------------------------------------------------------------------------\n")

                     else:
                                        print("\n                                                     You Loss this match.                                      ")
                                        print(f"\n                              Computer choice the  {computer} and  you choice {Player}.                       ")
                                        print("\n-------------------------------------------------------------------------------------------------------------------------\n")
                else:
                         print("\n------------------------------------------------------------------------------------------------------------------------\n")
                         print(" \n                                  OPPS! Something Is Wents Wrong.Try Again.......                                        ")
                         print("\n-------------------------------------------------------------------------------------------------------------------------\n")
                
     

        


    
        
        



