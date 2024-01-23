a=input("username:")
b=input("password:")
#a="sudhakar"
#b="selva"
if(a=="sudhakar" and b=="selva"):
    print("log in")
elif(a=="sudhakar" or b!="selva"):
        print("password entered wrong")
elif(a!="sudhakar" or b!="selva"):
            print("invalid details")
else:
    print("invalid user name")
a=