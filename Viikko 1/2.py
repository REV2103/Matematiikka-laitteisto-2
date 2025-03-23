import numpy as np

a = 1.6
b = 2.3
a_pot = a**2
b_pot = b**2
c = np.sqrt(a_pot+b_pot)
print(f"Suorakulmion joiden sivujen pituus on {a} ja {b} metriä, hypotenuusan pituus on {c:6.2f} metriä")
