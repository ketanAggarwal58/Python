def group_list(group, users):
    total = " "
    leng = len(users)
    for user in users:
        if users[leng-1] == user:
            total += user
        else:
            total += user +","+" "
    members = '{}:{}'.format(group, total)
    return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"