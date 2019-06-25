itemInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):

    totalItems = 0

    for item, quantity in inventory.items(): #calls the dictionary
        print(str(quantity)+ ' ' + item) #calls the quantity and then the nam
        totalItems += quantity # adds the total for the next print

    print('Total number of items: ' + str(totalItems)) 


displayInventory(itemInventory)


#next lesson

def addToInventory(inventory, addedItems):

    for item in addedItems:
        inventory.setdefault(item, 0) #adds default key of 0
        inventory[item] += 1 #increases value each time item appears
    return inventory

satchel = {'gold coin': 42, 'rope': 1}
displayInventory(satchel)
dragonLoot = ['gold coin','dagger', 'gold coin', 'gold coin', 'ruby']
satchel = addToInventory(satchel, dragonLoot)
displayInventory(satchel)

