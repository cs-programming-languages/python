# range is not widely used in modern python code
# not using range - enumerate
# prefer enumerate for counting

t = [443,223,5,1,6,34]

for i, v in enumerate(t):   # enumerate() yields (index,value) tuples and combining enumerate with tuple unpacking
    print("i={}, v={}".format(i,v))


print(list(range(0,10,3)))    # range(stop,start,step)

