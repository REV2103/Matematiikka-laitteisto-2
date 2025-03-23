import numpy as np

a = 2.493
b = 0.911
c = 137.7
d = 63.3

print(f" 1a: {np.degrees(a)} astetta")
print(f" 1b: {np.degrees(b)} astetta")
print(f" 2a: {np.radians(c)} radiaania")
print(f" 2b: {np.radians(d)} radiaania")

taulukko = np.array([30, 45, 60,90,120,135,150,180,270,360])
for i in taulukko:
    print(f"{i} astetta on {np.radians(i)} radiaania")