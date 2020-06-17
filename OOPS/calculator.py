# TODO: interface 

class interface:

     a = input("please enter your fisrt no.: \n")

     b = input("please enter your operator: \n")

     c = input("please enter your second no.: \n")
    
     def __init__(self):

        print("*"*20)

        # return True

# TODO: functionality

class function:

    def __init__(self):

        inf = interface()
        
        num1 = inf.a
        op = inf.b
        num2 = inf.c

        if op == '+':
       
            result = int(num1) + int(num2)

            print("result: "+str(result))

        elif op == '-':
            
            result = int(num1) - int(num2)

            print("result: "+str(result))

        elif op == '*':

            result = int(num1) * int(num2)

            print("result: "+str(result))

        elif op == '/':

            result = int(num1) / int(num2)

            print("result: "+str(result))

        else:

            print("Enter an valid operator")
            
        print("*"*20)

        # return True


fun = function()