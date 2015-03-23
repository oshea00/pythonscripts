
# create and use on-the-fly
print((lambda x: x**2)(4))

# filter
ints = range(1,50)
oddnums = filter(lambda x: x % 2,ints)
print oddnums

# map
squarednums = map(lambda x: x ** 2,ints)
print squarednums

# reduce
numtotal = reduce(lambda x,y: x + y,ints)
print numtotal

class Languages:
    "Some Test"

    def style(self,x):
        self.x = x

lan = Languages()

print(lan.x)

