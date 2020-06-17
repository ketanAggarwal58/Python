print("we have two types of loops in python");
print("1. for loop");
print("2. while loop");

print("this is an example of for loop");

for x in range(10):
    print(x);

for y in range(2,10):
    print(y);

print("this is an example of while loop");

i = 0;
while i < 7: 
    print(i);
    i += 1;
    if i == 5:
        print("code reaches to an impass");
        break; 