import Falserman as F

# Exmaple 1  :  Random Spawn English Name (100 times)
for i in range(1, 101):
    print(f"[{i}]  : {F.Spawner.name(1)[0]}")

# Exmaple 2  :  Random Spawn Mail (200 times)
for i in range(1, 201):
    print(f"[{i}]  : {F.Spawner.mail(1)[0]}")

# Exmaple 3  :  Random Spawn Phone Number (100 times)
for i in range(1, 101):
    print(f"[{i}]  : {F.Spawner.phonenumber(1, 11)[0]}")

# Exmaple 3  :  Random Spawn Passwords (200 times)
for i in range(1, 201):
    print(f"[{i}]  : {F.Spawner.password(1, inSymbol=False)[0]}")
