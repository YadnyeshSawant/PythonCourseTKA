casting1 = ["RD", "AK", "AB", "SB", "JF", "KS"]
casting2 = ["AA", "RM"]
casting3 = ["Tom Cruise"]
casting4 = ["AB", "MD", "Dharmedra"]
movies = {"Housefull5": casting1,"Pushpa2": casting2,"MissionImposible": casting3,"Sholay": casting4,}
# print("Movies ->", movies)
# print(movies["Housefull5"][0:len(movies["Housefull5"]):1])
print(type(movies.values()))
# for name in movies.keys():
#     print(name ,"--->",movies[name])
for data in movies.values():
    print(data)
    for cast in data:
        if cast == "AB":
            print(cast)
            
for k,v in movies.items():
    print(k,v)    