s = "JNdosfin8027340123490Jzsw234jjb4369kjbsdf8y" #Should have randomly generated string??

#Set some variables
alpha = ""
digit = ""

#Separate into alphas and digits
for ch in s:
    if(ch.isdigit()):
        digit += ch
    else:
        alpha += ch

print(alpha)
print(digit)

#Arrays for use in coming for loops
evenNum = []
ascEven = []
upperCh = []
ascCh = []

#Make a list of even numbers in the string
for i in digit:
    if int(i) % 2 == 0:
        evenNum.append(i)

#Make a list of the even numbers corresponding ASCII
for e in evenNum:
    ascEven.append(ord(e))

print(evenNum)
print(ascEven)

#Make a list of uppercase characters in string 
for ch in alpha:
    if(ch.isupper()):
        upperCh.append(ch)

#Make a list of the uppercase corresponding ASCII 
for ch in upperCh:
    ascCh.append(ord(ch))

print(upperCh)
print(ascCh)

