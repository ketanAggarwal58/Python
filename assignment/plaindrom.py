def plaindrome(n):
    temp = n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")

a = int(input("please enter any intger value: "))

plaindrome(a)