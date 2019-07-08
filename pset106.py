string1,string2 = input().split()

temp = string1
for i in range(len(string1)):
    temp = temp.replace(temp[i],string2[i])

if(temp == string2):
    print("yes")
else:
    print("no")
