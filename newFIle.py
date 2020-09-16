filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
 
for files in filenames:
    if(files.endswith('.hpp')):
        files = files.replace(".hpp", ".h")
        newfilenames.append(files)
        
    else:
        newfilenames.append(files)

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]