#!/usr/bin/python3
def main():

    def onStart():
        player1 = input("Enter your chance")
        player2 = input("Enter your chance")

        if(player1 == "rock" and player2 == "scissor"):
            print("Congratulations player1")
            restart = input("Do you want to restart?")
            if(restart == "yes"):
                onStart()
            else:
                print("Game completed!")

        elif(player2 == "rock" and player1 == "scissor"):
            print("Congratulations player2")
            restart = input("Do you want to restart?")
            if (restart == "yes"):
                onStart()
            else:
                print("Game completed!")


        elif(player1 == "rock" and player2 == "paper"):
            print("Congratulations player2")
            restart = input("Do you want to restart?")
            if (restart == "yes"):
                onStart()
            else:
                print("Game completed!")

        elif (player2 == "rock" and player1 == "paper"):
            print("Congratulations player1")
            restart = input("Do you want to restart?")
            if (restart == "yes"):
                onStart()
            else:
                print("Game completed!")

        elif(player1 == "scissor" and player2 == "paper"):
            print("Congratulations player1")
            restart = input("Do you want to restart?")
            if (restart == "yes"):
                onStart()
            else:
                print("Game completed!")

        elif (player2 == "scissor" and player1 == "paper"):
            print("Congratulations player2")
            restart = input("Do you want to restart?")
            if (restart == "yes"):
                onStart()
            else:
                print("Game completed!")
        else:
            print("Game draw")
            restart = input("Do you want to restart?")
            if (restart == "yes"):
                onStart()
            else:
                print("Game completed!")
    onStart()

if __name__== "__main__": main()