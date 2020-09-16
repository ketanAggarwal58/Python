def guest_list(guests):
    for guest in guests:
        name = guest[0]
        age = guest[1]
        profession = guest[2]
        print('{} is {} years old and works as {}'.format(name, age, profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])