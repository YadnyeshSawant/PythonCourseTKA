#Encapsulation
class Student:

    def __init__(self, n, r, m,p):
        self.__name = n
        self.__roll = r
        self.__subjectMarks = m
        self.__pin = p   
        
    def getName(self):
        if(self.__pin == 1234):
            return self.__name
        else:
            print("INVALID PIN")
        
    def setName(self,newName):
        if(self.__pin == 1234):
            self.__name = newName
            return self.__name
        else:
            print("INVALID PIN")
            
    def getRoll(self):
        if(self.__pin == 1234):
            return self.__roll
        else:
            print("INVALID PIN")
        
    def setRoll(self,newRoll):
        if(self.__pin == 1234):
            self.__roll = newRoll
            return self.__roll
        else:
            print("INVALID PIN")
        
    def getMarks(self):
        if(self.__pin == 1234):
            return self.__subjectMarks
        else:
            print("INVALID PIN")
        
    def setMarks(self,newMarks):
        if(self.__pin == 1234):
            self.__subjectMarks = newMarks
            return self.__subjectMarks
        else:
            print("INVALID PIN")
            
st = Student("Yadnyesh",101,89,1234)

st.__name ="shree"

print(st.getName())
print(st.getRoll())
print(st.getMarks())

print(st.setName("Ujwal"))
print(st.setRoll(203))
print(st.setMarks(56))