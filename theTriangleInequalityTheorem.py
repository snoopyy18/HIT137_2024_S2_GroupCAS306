import sys



#Defining some variables 
total = 0 
error = 0 

#Intro
print("The Triangle Inequality Theorem")

print("********************************")

print("This program checks if the three user inputs can form a triangle.")

print("")

print("**Enter q at any time to quit.**")

print("")



#Defining some functions used throughout

#This function "check" is the triangle inequality theorem. Adding the total at the end is used to check if any of the checks is valid, as you need to check all six variations of the sides
def check(sOne, sTwo, sThree):
    global total
    
    if sOne + sTwo > sThree and sOne + sThree > sTwo and sTwo + sThree > sOne:
        total = total + 1

#This function qat (quit and try) is basically just there so I don't have to constantly type the same thing. 
def qat(side):
    global error 

    if side == 'q': #I couldn't get something like if side == 'q' or 'Q' working, I'm guessing it's incorrect syntax or something. It would just quit off of any text IIRC
        sys.exit()
    elif side == 'Q':
        sys.exit()
        

    try:
        float(sOne)
    except ValueError:
        print("Cannot float a string. Try again.")
        print("")
        error = 1 #The error is there so that we can know in the parent indentation if we received an error 


#The main program
while True:

    while True:
        print("Please enter the first side:")
        sOne = input()

        qat(sOne) 
        if error == 1: #here we can see the "error" variable I defined before become of use. Not sure if there is an easier/better way about it 
            error = 0 
            continue 

        print("")
        break
    

    while True:
        print("Please enter the second side:")
        sTwo = input()

        qat(sTwo)
        if error == 1:
            error = 0 
            continue

        print("")
        break 


    while True:
        print("Please enter side three:")
        sThree = input()

        qat(sThree)
        if error == 1:
            error = 0
            continue

        print("")
        break

#Running through all variations. There has to be a better way to do this, probably in the math library or something but I'm too lazy to find and learn. 
#This needs to happen because if you ran only one of the variations, with say for example sides 3, 3, 1, it would work. Then if you ran 3, 1, 3 it would say not a triangle.
    check(sOne, sTwo, sThree)
    check(sOne, sThree, sTwo)
    check(sTwo, sOne, sThree)
    check(sTwo, sThree, sOne)
    check(sThree, sOne, sTwo)
    check(sThree, sTwo, sOne)

    if total > 1:
        print("********************\n This is a triangle\n********************")
        print("")
    else:
        print("************************\n This is NOT a triangle\n************************")
        print("")
    
#Resetting total for another while loop
    total = 0 
    

    
        