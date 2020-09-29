# Write a python function to get the reverse of a number.

def reverse_no(n):
    reverse = 0
    while(n>0):
        remainder = n%10
        reverse = (reverse*10) + remainder
        n = n//10
    return "{} is the reverse no. ".format(reverse)

a = int(input("please enter an integer value: "))

print(reverse_no(a))