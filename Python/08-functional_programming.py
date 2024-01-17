#Functional Programming Paradigm, in which functions are treated as values just like any other variable.
#DECORATOR:  higher-order function that can modify another function.
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

#decorator that announces when a function is about to begin, and when it ends
# call it using an @ symbol
@announce
def hello():
    print("Hello, World!")

hello()

#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
# This can be useful when we don’t want to write a whole separate function for a single, small use.
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lambda person: person["name"])
# def f(person):
#     return person["name"]

# people.sort(key=f)

print(people)