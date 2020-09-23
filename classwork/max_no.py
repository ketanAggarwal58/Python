def max(a,b,c):
    if a>b and a>c:
        print(a+" is greater than "+b+","+c)
    elif b>a and b>c:
        print(b+" is greater than "+a+","+c)
    elif c>a and c>b:
        print(c+" is greater than "+a+","+b)
    else:
        print("all the no. are eqaul")

print("please enter your first no. ")
d = input()

print("please enter your second no. ")
e = input()

print("please enter your third no. ")
f = input()

max(int(d),int(e),int(f))