import moviesDb

actorName = input("Enter the name of the Actor  ")
count = 0
movie = []
year = []
for k,v in moviesDb.moviesData.items():
    for k1,v1 in v.items():
        for actor in v1:
            if actor == actorName:
                count += 1
                movie.append(k1)
                year.append(k)
                
print("------------------------------------------")

print("Actor Name =", actorName)
for i in range(0,count):
    print(f"Movie Name = {movie[i]} ({year[i]})")
# print("Year of Release =", year)
# print("Name of Movie =",movie)
print("Number of the time stared in movie = ", count)

print("------------------------------------------")

###################################################
# OUTPUT
# Enter the name of the Actor  Akshay Kumar
# ----------------------------------------
# Actor Name = Akshay Kumar
# Movie Name = Atrangi Re (2021)
# Movie Name = Bachchhan Paandey (2022)
# Number of the time stared in movie =  2
# ----------------------------------------