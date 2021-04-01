# Statically typed - If the type of variable is known at compile time.
# int score =10 can be written as score = 10

# Dybamically typed - If the type is associated with run-time values and not with named variables. Values tored in variable hav type and not the name or the variable itself. 

# Variable types
# Numbers: Integers, Floating point and Complex numbers
# Booleans: Loval values indicating False, True and None
# Strings: Ordered sequence of characters
# Lists: Ordered mutable sequence of objects 
# Tuples: Orderd immutable sequence of objects
# Sets: Mutable collections of unordered unique objects
# FrozenSets: Immutable collections of unordered unique objects 
# Dictionaries: Collections of unordered key: Value pairs

score = 10
type(score) # this will return <type 'int'>

name = 'Harry'
type(name) # this will return <type 'str'>

id(score) # this returns the memory value of the variable
print(hex(id(name))) # this returns HEX value for the memory location of the variable

years = [2001, 2002, 2003] # Data type is List

Value = (1, 'John', 3) # This is a Tuple

vowels = {'a','e','i','o','u'} #this is a set, containing unique data types

person = {'name':'Harry', 'location':'Netherlands'} #This is a Dict (Dictionary)

fs = frozenset ((1,2,'abc','xyz')) #this is a frozen set

