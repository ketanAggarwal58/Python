"""

    The replace_ending function replaces the old string in a sentence with the new string,
    but only if the sentence ends with the old string. If there is more than one occurrence 
    of the old string in the sentence, only the one at the end is replaced, not all of them. 
    For example, replace_ending("abcabc", "abc", "xyz") should 
    return abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive, 
    so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made). 

 """

def replace_ending(sentence, old, new):
    a = sentence.find(old)
    b = len(old)
    c = len(sentence)
    d = int(c)-int(b)
    e = sentence[int(d):]

    if e == old:
        i = int(d)
        new_sentence = sentence[:i] + e.replace(old, new)
        return new_sentence
    return sentence

weather = 'rainfall'

print(weather[:4])

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
print(replace_ending("The weather is nice in May", "may", "april"))
print(replace_ending("The weather is nice in May", "May", "April")) 
