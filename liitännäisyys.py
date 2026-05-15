import numpy as np

a = np.float32(2**25)
b = np.float32(-(2**25))
c = np.float32(1.0)

l1 = a + (b + c)
l2 = (a + b) + c

print(f"a + (b + c) = {l1}")
print(f"(a + b) + c = {l2}")
