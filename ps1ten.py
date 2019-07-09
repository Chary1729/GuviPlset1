st1,st2 = input().split()

tp = st1
for i in range(len(st1)):
    tp = tp.replace(tp[i],st2[i])

if(tp == st2):
    print("yes")
else:
    print("no")
