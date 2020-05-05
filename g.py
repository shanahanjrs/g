class p_class:
    """
    With newline:
    >>> p+'mystr'
    >>> mystr

    Without newline:
    >>> p-'mystr'
    >>> mystr>>>
    """
    def __init__(self):
        pass
    def __add__(self, o):
        print(o)
    def __sub__(self, o):
        print(o, end='')

p = p_class()

"""
short builtins
"""
a = all
ab = abs
an = all
ac = ascii

b = bin

e = enumerate
ev = eval
ex = exec

f = filter

fr = format

h = hex

ip = input
it = iter

l = len

m = map
mx = max
mn = min

o = ord
oc = oct

pw = pow

# Write own range()

rv = reversed
rd = round

s = str
st = sorted
sm = sum

t = tuple
tp = type

z = zip

"""
shortcuts
"""
V = 'aeiou'
C = 'bcdfghjklmnpqrstvwxyz'
T = True
F = False

