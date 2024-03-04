# Method 1 : Aliasing Modules
# Alias the name by using 'as' keyword
import math as m

# Once we alias a module, The original name of the module will be unaccessible.
# We can simply use m instead of math.
print(m.sin(m.pi/2))

# Method 2 : Aliasing the Entities
# We can alias the entities also from the modules
from math import sin as SIN, pi as P

print(SIN(P/2))