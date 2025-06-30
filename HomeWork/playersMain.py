class Player:

    def __init__(self, j, n, rs, w, t):
        self.__jerseyNo = j
        self.__name = n
        self.__runsScored = rs
        self.__wickets = w
        self.__team = t

    def get_jerseyNo(self):
        return self.__jerseyNo

    def set_jerseyNo(self, j):
        self.__jerseyNo = j

    def get_name(self):
        return self.__name

    def set_name(self, n):
        self.__name = n

    def get_runsScored(self):
        return self.__runsScored

    def set_runsScored(self, rs):
        self.__runsScored = rs

    def get_wickets(self):
        return self.__wickets

    def set_wickets(self, w):
        self.__wickets = w

    def get_team(self):
        return self.__team

    def set_team(self, t):
        self.__team = t


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
    tname = input("Enter the Team Name") + "Team"
    print("OPTION 1: GET ALL BATSMAN ")
    print("OPTION 2: GET ALL BWOLERS ")
    print("OPTION 3: GET ALL PLAYERS ")
    print("OPTION 4: GET ALLROUNDERS ")

    print("ENTER YOUR CHOICE")
    option = int(input("Enter Your Option"))

    if option == 1:
        getBatsman(tname)
    elif option == 2:
        getBolwer(tname)
    elif option == 3:
        getTeamDetails(tname)
    elif option == 4:
        getAllRounders(tname)


miTeam = []
rcbTeam = []
cskTeam = []

p1 = Player(45, "Rohit Sharma", 6211, 27, "MI")
p2 = Player(63, "Ishan Kishan", 2328, 34, "MI")
p3 = Player(93, "Suryakumar Yadav", 3248, 58, "MI")
p4 = Player(33, "Hardik Pandya", 1535, 53, "MI")
p5 = Player(99, "Jasprit Bumrah", 68, 154, "MI")
p6 = Player(77, "Tilak Varma", 925, 46, "MI")
p7 = Player(55, "Tim David", 872, 21, "MI")
p8 = Player(19, "Gerald Coetzee", 40, 17, "MI")
p9 = Player(90, "Piyush Chawla", 599, 179, "MI")
p10 = Player(11, "Akash Madhwal", 20, 15, "MI")
p11 = Player(27, "Nehal Wadhera", 241, 13, "MI")

p12 = Player(7, "MS Dhoni", 5243, 25, "CSK")
p13 = Player(9, "Ruturaj Gaikwad", 1797, 33, "CSK")
p14 = Player(8, "Ravindra Jadeja", 2692, 152, "CSK")
p15 = Player(33, "Shivam Dube", 1521, 4, "CSK")
p16 = Player(90, "Matheesha Pathirana", 20, 35, "CSK")
p17 = Player(99, "Deepak Chahar", 79, 73, "CSK")
p18 = Player(5, "Moeen Ali", 1130, 33, "CSK")
p19 = Player(19, "Tushar Deshpande", 12, 32, "CSK")
p20 = Player(20, "Maheesh Theekshana", 25, 36, "CSK")
p21 = Player(44, "Ajinkya Rahane", 4433, 19, "CSK")
p22 = Player(21, "Ben Stokes", 935, 28, "CSK")

p23 = Player(18, "Virat Kohli", 7900, 5, "RCB")
p24 = Player(97, "Faf du Plessis", 4500, 36, "RCB")
p25 = Player(5, "Glenn Maxwell", 2800, 34, "RCB")
p26 = Player(19, "Dinesh Karthik", 4516, 42, "RCB")
p27 = Player(10, "Mohammed Siraj", 42, 78, "RCB")
p28 = Player(6, "Cameron Green", 500, 12, "RCB")
p29 = Player(15, "Rajat Patidar", 861, 22, "RCB")
p30 = Player(70, "Karn Sharma", 245, 69, "RCB")
p31 = Player(31, "Yash Dayal", 15, 21, "RCB")
p32 = Player(13, "Anuj Rawat", 393, 17, "RCB")
p33 = Player(54, "Mayank Dagar", 72, 13, "RCB")


miTeam.append(p1)
miTeam.append(p2)
miTeam.append(p3)
miTeam.append(p4)
miTeam.append(p5)
miTeam.append(p6)
miTeam.append(p7)
miTeam.append(p8)
miTeam.append(p9)
miTeam.append(p10)
miTeam.append(p11)

cskTeam.append(p12)
cskTeam.append(p13)
cskTeam.append(p14)
cskTeam.append(p15)
cskTeam.append(p16)
cskTeam.append(p17)
cskTeam.append(p18)
cskTeam.append(p19)
cskTeam.append(p20)
cskTeam.append(p21)
cskTeam.append(p22)

rcbTeam.append(p23)
rcbTeam.append(p24)
rcbTeam.append(p25)
rcbTeam.append(p26)
rcbTeam.append(p27)
rcbTeam.append(p28)
rcbTeam.append(p29)
rcbTeam.append(p30)
rcbTeam.append(p31)
rcbTeam.append(p32)
rcbTeam.append(p33)

# menu()
getBatsman(miTeam)