from Item import Item

item1 = Item("MyItem", 750)

# Setting an attributes
item1.__price = 900
item1.apply_increment(0.25)
# Getting an attributes
print(item1.price)
