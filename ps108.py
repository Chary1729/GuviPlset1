my_input=input()
i=1
print(my_input[0].upper(),end="")
while i<len(my_input):
    if ((my_input[i].isspace()) == True):
        i+=1
        print(end=" ")
        print(my_input[i].upper(),end="")
    else:
        print(my_input[i],end="")
    i+=1
