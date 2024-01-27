from kanren import run, fact, var
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative

addition = "add"
multiplication = "mul"

fact(commutative, multiplication)
fact(commutative, addition)
fact(associative, multiplication)
fact(associative, addition)

# Variables
x, y, z = var('a'), var('b'), var('c')

# Corrected code for defining the relation
originalPattern=(multiplication,(addition, z, x),y)

# Example expression
ex1 = (multiplication, 9, (addition, 5, 1))
ex2 = (addition,5,(multiplication,8,1))
ex3=(multiplication,59,(addition,234,34))

# Corrected code for using eq
print(run(0, (x, y, z), eq(originalPattern,ex1)))
print(run(0, (x, y, z), eq(originalPattern,ex2)))
print(run(0, (x, y, z), eq(originalPattern,ex3)))
