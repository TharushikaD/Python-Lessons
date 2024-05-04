x = "Python{}"
y = "Elephant"
z = """\nHellow World"""

# print(x)
# print(type(x))
# print(type(x), x)
#checked the type
print(x,y,z)
print(x[0])
print(x[4]) 
# this can also be done by -2

a = 0
print(type(a))
print(x.format(a))
print(x)
print(x + y+ str(a))

# another way to use formatt
print(f"White {y}")

b = 0.0
print(type(b))

print("Configure git")

# List
l1= [1,2,3,"Tharushika",0.0]
print(l1[3])
print(l1[0:4])
print(len(l1))

# Tuple
# Tuples cant be changed they are immutable
tuple1 = (1,2,3,4)
print(tuple1)

# Boolean
is_created = False
is_Fail = True
print(is_created, type(is_created))

if 2> 0 :
    is_created = True

    print(is_created)

# Set..
set1 = set(['A','F',1,2,3,3,3,3,3])
print(set1)

set2 = set(['A','F',1,2,3,3,3,3,3])
print(set2)

# dictionary..
dict={}
dict1 = {
    "name" : "Tharushika",
    "age" : 22,
    "mobile": "111111"
}

dict2 = {
    "name" : "Dilmini",
    "age" : 22,
    "mobile": "2222"
}

print(dict)
print(dict1["mobile"])

list = []
list.append(dict1)
list.append(dict2)
print(list)

import pandas as pd
df = pd.DataFrame(list)
print(df.head())
print(type(df))







