def sortstuffwithsomethingelse(list,otherlist):
    v = len(list)
    for a in range(0,v**2):
        for i in range(0, v - 1):
            if(list[i] > list[i + 1]):
           	   v1 = list[i]
           	   list[i] = list[i + 1]
           	   list[i + 1] = v1
           	   v2 = otherlist[i]
           	   otherlist[i] = otherlist[i+1]
           	   otherlist[i+1] = v2
            for p in range(0, v - 1):
              if(list[p] > list[p + 1]):
                 v3 = list[p]
                 list[p] = list[p + 1]
                 list[p + 1] = v3;
                 v4 = otherlist[p]
                 otherlist[p] = otherlist[p+1]
                 otherlist[p+1] = v4
    return list, otherlist
userinput = input("Input something: ")
new = userinput.lower()
userlist = list(new)
listofnumbers = []
listofpositions = []
listofletters = ['a','b','c','d','e','f','g','h','i','j', 'k', 'l', 'm', 'n','o','p', 'q', 'r', 's', 't','u', 'v', 'w', 'x','y', 'z']
for character in userlist:
    for i in range(0, len(listofletters)):
        if character == listofletters[i]:
            listofpositions.append(i+1)
listofpositions,userlist = sortstuffwithsomethingelse(listofpositions,userlist)
finallist = []
for i in range(0, len(userlist)):
    finallist.append(userlist[len(userlist)-1-i])
print(''.join(finallist))
