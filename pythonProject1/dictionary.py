dict = {"name": "hiba", "age": "24", "profession": "engineer"}
print(dict)

#dictionary methods
marks = {"hiba": 98, "harry": 65, "taha": 78}
marks.pop("hiba")
print(marks)
#print(marks.get("harry")) #fetch the marks of 'harry'
#another way of get() method
#print(marks["harry"])
print(marks.keys()) #fetch the keys
print(marks.values()) #return values only
print(marks.items()) #return tuples
marks.update(harry = 70) #dictionary is mutable b/c it can be modified
print(marks)
