# decorator function that always subtracts greater number from smaller
def subModified(funct):
    def inner(a, b):
        if a < b:
            temp = a
            a = b
            b = temp
        funct(a, b)
    return inner

    
@subModified  # used decorator
def subtract(a, b):
    print(a - b)  # this funtion subtracts b from a 
    

# another way to decorate a function
decorated = subModified(subtract)


subtract(3, 4)  # function call
decorated(3, 4)  # function call for Decorator Without @ Syntax


###############################################################
# CONCLUSION:-
# The subtract function prints the result of subtracting b from a, but when decorated with @subModified, it ensures the larger number is always subtracted from to avoid negative results