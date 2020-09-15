""" Let's create a function that turns text into pig latin: a simple text transformation that 
modifies each word moving the first character to the end and appending "ay" to the end. 
For example, python ends up as ythonpay. """

def pig_latin(text):

    say = text.split()
    words = say
    count = 0
    new_list = []
    for word in words:
        if(len(words) >= count):
            latin_pig = word[1:]+word[0]+"ay"
            new_list.insert(count, latin_pig)
            count = count + 1
    return convert(new_list)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"