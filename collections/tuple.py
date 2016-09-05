# A mutable object can be changed after it's created, and an immutable object can't.

# hetergeneous (different type of mixture) vs homogeneous (same type of mixture)

#TUPLE is hetergeneous immutable sequence (once created cannot be removed and replaced)

my_tuple = ("t3","t2",1)

print(my_tuple)

print(my_tuple[2])                                  # access tuple using square brackets []

print(len(my_tuple))                                # determine the length of the tuple

for item in my_tuple:                               # iterate over the tuple by using for each loop
    print(item)

my_concat_tuple = my_tuple + ("t4","t5")            # concatination with + operator and creating new tuple

print(my_concat_tuple)

print(my_tuple * 3)                                 # can be repeated by usign multiplication operator but not changing the original tuple

print(my_tuple)

my_nested_tuple = ((200,204),(300,304),(400,404))

print(my_nested_tuple[0][1])

my_single_tuple = (1,)                              # including trailing comma

print(my_single_tuple)

print(type(my_single_tuple))

my_empty_tuple = ()

print(type(my_empty_tuple))

my_wo_parentheses_tuple = 1, 2, 3, 4, 5, 6, 7, "Hello"  # this feature can be used to return multiple values from a function

print(my_wo_parentheses_tuple)
print(type(my_wo_parentheses_tuple))


def minmax(items):                                  # return multiple values
    return min(items), max(items)

min_val, max_val = minmax([54,3,2,6,43,76,99])      # tuple unpacking allows us to destructure into named references

print("Min value = ",min_val)

print("Max value =",max_val)

(a,b,(c,d)) = (4,6,(1,2))                           # tuple unpacking works with arbitrarly nested tuples

print("a:",a)

print("b:",b)

a,b = b,a                                           # a,b = b,a  is the idiomatic Python swap

print("After swap a,b = b,a")

print("a:",a)

print("b:",b)

my_tuple_from_other_data_structure = tuple("HEllo World")   # use tuple constractor to create a new tuple from other data structure
print(my_tuple_from_other_data_structure)

print(5 in (2,3,5,1))                               # in and not in operators can be used with tuple





