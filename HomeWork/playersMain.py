import playersInfo as pi 

def getBatsman(team):
    for p in range(len(team)):
        if team[p].get_runsScored() > 1000:
            print(f"{'TEAM NAME:':<15} {team[p].get_team()}")
            print(f"{'JERSEY NO:':<15} {team[p].get_jerseyNo()}")
            print(f"{'PLAYER NAME:':<15} {team[p].get_name()}")
            print(f"{'RUNS SCORED:':<15} {team[p].get_runsScored()}")
            print(f"{'WICKETS:':<15} {team[p].get_wickets()}")
            print("-" * 40)


def getBolwer(team):
    for p in range(len(team)):
        if team[p].get_wickets() > 20:
            print(f"{'TEAM NAME:':<15} {team[p].get_team()}")
            print(f"{'JERSEY NO:':<15} {team[p].get_jerseyNo()}")
            print(f"{'PLAYER NAME:':<15} {team[p].get_name()}")
            print(f"{'RUNS SCORED:':<15} {team[p].get_runsScored()}")
            print(f"{'WICKETS:':<15} {team[p].get_wickets()}")
            print("-" * 40)


def getAllRounders(team):
    for p in range(len(team)):
        if team[p].get_wickets() > 20 and team[p].get_runsScored() > 1000:
            print(f"{'TEAM NAME:':<15} {team[p].get_team()}")
            print(f"{'JERSEY NO:':<15} {team[p].get_jerseyNo()}")
            print(f"{'PLAYER NAME:':<15} {team[p].get_name()}")
            print(f"{'RUNS SCORED:':<15} {team[p].get_runsScored()}")
            print(f"{'WICKETS:':<15} {team[p].get_wickets()}")
            print("-" * 40)


def playerDetails(player):
    print(f"{'TEAM NAME:':<15} {player.get_team()}")
    print(f"{'JERSEY NO:':<15} {player.get_jerseyNo()}")
    print(f"{'PLAYER NAME:':<15} {player.get_name()}")
    print(f"{'RUNS SCORED:':<15} {player.get_runsScored()}")
    print(f"{'WICKETS:':<15} {player.get_wickets()}")
    print("-" * 40)


def getTeamDetails(team):
    count = 1
    for p in range(len(team)):
        print(f"{'TEAM NAME:':<15} {team[p].get_team()}")
        print(f"{'PLAYER NO:':<15} {count}")
        print(f"{'JERSEY NO:':<15} {team[p].get_jerseyNo()}")
        print(f"{'PLAYER NAME:':<15} {team[p].get_name()}")
        print(f"{'RUNS SCORED:':<15} {team[p].get_runsScored()}")
        print(f"{'WICKETS:':<15} {team[p].get_wickets()}")
        print("-" * 40)
        count += 1


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
            getBatsman(tname)
            
        elif option == 2:
            tname = input("ENTER TEAM NAME IN SMALL CASE \t")
            if tname == "mi":
                tname = pi.miTeam
            elif tname == "rcb":
                tname = pi.rcbTeam
            elif tname == "csk":
                tname = pi.cskTeam

            getBolwer(tname)

        elif option == 3:
            tname = input("ENTER TEAM NAME IN SMALL CASE \t")
            if tname == "mi":
                tname = pi.miTeam
            elif tname == "rcb":
                tname = pi.rcbTeam
            elif tname == "csk":
                tname = pi.cskTeam
            getTeamDetails(tname)

        elif option == 4:
            tname = input("ENTER TEAM NAME IN SMALL CASE \t")
            if tname == "mi":
                tname = pi.miTeam
            elif tname == "rcb":
                tname = pi.rcbTeam
            elif tname == "csk":
                tname = pi.cskTeam
            getAllRounders(tname)

        elif option == 5:
            playerName = input("ENTER PLAYER NAME \t")
            tname = input("ENTER TEAM NAME OF THE PLAYER IN SMALL CASE \t")
            playerName = input("ENTER PLAYER NAME \t")
            tname = input("ENTER TEAM NAME OF THE PLAYER IN SMALL CASE \t")
            playerDetails(playerName)


menu()