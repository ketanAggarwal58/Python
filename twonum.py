print("please enter your first no. ")
a = input()

print("please enter your second no.")
b = input()

if(int(a)>int(b)):
    print(a+" is greater than "+b)
elif(int(b)>int(a)):
    print(b+" is greater than "+a)
else:
    print(a+" and "+b+" are equal")
