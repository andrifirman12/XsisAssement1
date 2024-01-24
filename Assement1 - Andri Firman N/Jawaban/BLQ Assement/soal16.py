
menus = [
    ("Tuna Sandwich", 42),
    ("Spaghetti Carbonara", 50),
    ("Tea pitcher", 30),
    ("Pizza", 70),
    ("Salad", 30)
]
people = 4
people_alergic_fish = 1
charge_for_all = 0

for i in range (0, len(menus)):
    if "Tuna" in menus[i][0]:
        tax = menus[i][1]*0.10
        service = menus[i][1]*0.05
        ttl_fish = menus[i][1] + tax + service
    else:
        tax = menus[i][1]*0.10
        service = menus[i][1]*0.05
        ttl = menus[i][1] + tax + service
        charge_for_all = charge_for_all + ttl

charge_for_alergic = charge_for_all/people
charge_for_other = charge_for_alergic + (ttl_fish/(people -people_alergic_fish))
div = "--------------------------------------------------------------------------------"

print(div)
print(f'''For Person who has alergic fish ({people_alergic_fish}) he is charge {charge_for_alergic}, \nand for the other ({people -people_alergic_fish}) is charge {charge_for_other}''')
print(div)