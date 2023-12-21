from shop import PetShop
import sys


petshop = PetShop("mysql","root", "qwerty1234")
petshop.create_shop()
ids = petshop.add_item("Mikky mouse", 100)
print(ids)
for id in ids:
    res = petshop.delete_item_by_id(id)
