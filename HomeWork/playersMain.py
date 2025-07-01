import playersInfo as pi 

def menu():
    tname = ""
    option = 0
    while True:
        print("OPTION 1: GET ALL BATSMAN ")
        print("OPTION 2: GET ALL BWOLERS ")
        print("OPTION 3: GET ALL PLAYERS ")
        print("OPTION 4: GET ALLROUNDERS ")
        print("OPTION 5: GET PLAYER DETAILS ")

        option = int(input("ENTER YOUR CHOICE\t"))
        if option == 1:
            tname = input("ENTER TEAM NAME IN SMALL CASE \t")
            if tname == "mi":
                tname = pi.miTeam
            elif tname == "rcb":
                tname = pi.rcbTeam
            elif tname == "csk":
                tname = pi.cskTeam
            pi.getBatsman(tname)
            
        elif option == 2:
            tname = input("ENTER TEAM NAME IN SMALL CASE \t")
            if tname == "mi":
                tname = pi.miTeam
            elif tname == "rcb":
                tname = pi.rcbTeam
            elif tname == "csk":
                tname = pi.cskTeam

            pi.getBolwer(tname)

        elif option == 3:
            tname = input("ENTER TEAM NAME IN SMALL CASE \t")
            if tname == "mi":
                tname = pi.miTeam
            elif tname == "rcb":
                tname = pi.rcbTeam
            elif tname == "csk":
                tname = pi.cskTeam
            pi.getTeamDetails(tname)

        elif option == 4:
            tname = input("ENTER TEAM NAME IN SMALL CASE \t")
            if tname == "mi":
                tname = pi.miTeam
            elif tname == "rcb":
                tname = pi.rcbTeam
            elif tname == "csk":
                tname = pi.cskTeam
            pi.getAllRounders(tname)

        elif option == 5:
            playerName = input("ENTER PLAYER NAME \t")
            tname = input("ENTER TEAM NAME OF THE PLAYER IN SMALL CASE \t")
            playerName = input("ENTER PLAYER NAME \t")
            tname = input("ENTER TEAM NAME OF THE PLAYER IN SMALL CASE \t")
            pi.playerDetails(playerName)


menu()