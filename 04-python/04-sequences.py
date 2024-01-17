#STRING
namea = "Abdelkhalek"
print(namea[0])


#LIST - sequence if mutable values
#Define a list of names
names = ["Abdelkhalek", "Boutahri", "1337", "42"]
#add name to the list
names.append("Benguerir") 
print(names)
print(names[3])


#TUPLE - sequence of immutuable values (can't change/add, typical order)
coordinateX = 10.0
coordinateY = 20.0
coordinate = (10.0, 20.0)


#SET - collection of unique values (efficient, if you don't care about order)
#Create an empty set
s = set()
# Add elements to set
s.add(1)
s.add(100)
s.add(512)
s.add(100)
s.add(99)
s.add(52)
s.remove(512)
print(s)
# print the Len. of set
print(f"The set has {len(s)} elemnts.")


#LOOPS -
for i in [0, 1, 2, 3, 4, 5]:
    print(i)

for i in range(6):
    print(i)

for name in names:
    print(name)

for character in namea:
    print(character)


#DICT - collection of key-value pairs (powerful ex: key:word, value:definitions)
houses = {"1337": "Benguerir","42":"Paris"}
print(houses["42"])
print(houses["1337"])
houses["21"] = "Moscow"
print(houses["21"])