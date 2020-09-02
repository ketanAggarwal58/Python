print("please enter your first no. ")
a = input()

print("please enter your second no.")
b = input()

print("please enter your third no")
c = input()

if((int(a)>int(b)) and (int(a)>int(c))):
    print(a+" is greater than "+b+" and "+c)
elif((int(b)>int(a)) and (int(b)>int(c))):
    print(b+" is greater than "+a+" and "+c)
elif((int(c)>int(a)) and int(c)>int(b)):
    print(c+" is greater than "+a+" and "+b)
else:
    print(a+ " "+b+" and "+c+ " are equal")
