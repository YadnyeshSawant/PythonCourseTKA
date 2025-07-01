import playersInfo as pi 
option = 0

def menu():
    tname = ""
    response = "y"
    global option
    while option !=6:
        print("-" * 40)
        print("OPTION 1: GET ALL BATSMAN ")
        print("OPTION 2: GET ALL BWOLERS ")
        print("OPTION 3: GET ALL PLAYERS ")
        print("OPTION 4: GET ALLROUNDERS ")
        print("OPTION 5: GET PLAYER DETAILS ")

        option = int(input("ENTER YOUR CHOICE\t"))
        print("-" * 40)
        if option == 1:
            tname = pi.setTeam()
            pi.getBatsman(tname)
            
        elif option == 2:
            pi.setTeam()
            pi.getBolwer(tname)

        elif option == 3:
            pi.setTeam()
            pi.getTeamDetails(tname)

        elif option == 4:
            pi.setTeam()
            pi.getAllRounders(tname)

        elif option == 5:
            playerName = input("ENTER PLAYER NAME \t")
            tname = pi.setTeam()
            pi.playerDetails(playerName,tname)
        elif option == 6:
            break
    

menu()