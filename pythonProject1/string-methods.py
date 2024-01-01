name = "hibbaa"
print(name)

#string slicing
print(name[0:3]) #starts from '0' and go all the way to '2'
print(name[1:3]) #starts from '1' and go all the way to '2'

#string methods
print(name.isalnum())
print(name.capitalize())
print(name.count("b"))

#multi-line string
lyrics = '''I'm a barbie girl!!
in the barbie worldd!!'''

lyrics[0] = "hiba" #str in immutable & hence this line throws an error
print(lyrics)
#print(lyrics)