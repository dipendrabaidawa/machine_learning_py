from numpy.lib.function_base import average


speed = [32,111,138,28,59,77,97]

a = average(speed)
s = 0
for v in speed:
    s += abs(a-v)

print(s, s/7)