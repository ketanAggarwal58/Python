def format_address(address_string):

    h_no = ""
    street = ""
    new  = address_string.split()
    
    for address in new:
        if(address.isnumeric()):
            h_no = address
        else:
            street += address +" "
    return "house number {} on street named {}".format(h_no, street)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
