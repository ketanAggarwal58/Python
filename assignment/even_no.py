def even_no(n):
    for x in n:
        if x%2 == 0:
            print(str(x)+" is a even no.")
        else:
            print(str(x)+" is a odd no.")

a = [1,2,3,4,5,6,7,8,9]

even_no(a)