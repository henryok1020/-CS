# inventory.py
stuff = {'rope':3, 'torch': 7, 'gold coin': 52, 'dagger': 1, 'arrow': 11 }

def displayInventory(inventory):
    total_items=0
    for item in inventory:
        print(str(inventory[item])+''+item)
        total_items += inventory[item]
    print("Total number of items:"+str(total_items))

displayInventory(stuff)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] +=1
    return inventory
inv = {'gold coin':31, 'rope': 1}
displayInventory(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)