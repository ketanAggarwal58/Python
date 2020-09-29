# Write a Python function that takes a number as a parameter and check the number is
# prime or not.

def prime_no(n):
    if n > 1:
        for i in range(2, n):
            if(n%2) == 0:
                break
            else:
               return "{} is a prime no.".format(n)

a = int(input("please enter an integer value: "))

print(prime_no(a))