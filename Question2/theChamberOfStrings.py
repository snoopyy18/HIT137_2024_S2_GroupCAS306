s = "JNdosfin8027340123490Jzsw234jjb4369kjbsdf8y"


alpha = ""
digit = ""

for char in s:
    if(char.isdigit()):
        digit += char
    else:
        alpha += char

print(alpha)
print(digit)
