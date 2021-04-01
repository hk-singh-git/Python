# Statically typed - If the type of variable is known at compile time.
# int score =10 can be written as score = 10

# Dybamically typed - If the type is associated with run-time values and not with named variables. Values tored in variable hav type and not the name or the variable itself. 

score = 10

type(score) # this will return <type 'int'>

name = 'Harry'

type(name) # this will return <type 'str'>

id(score) # this returns the memory value of the variable

hex(id(name)) # this returns HEX value for the memory location of the variable

