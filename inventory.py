SIZE = 10
inventory = ["Empty"] * SIZE
 
 
def add_item(item):
    for i in range(SIZE):
        if inventory[i] == "Empty":
            inventory[i] = item
            return True
    return False
 
 
def remove_item(item):
    for i in range(SIZE):
        if inventory[i] == item:
            inventory[i] = "Empty"
            return True
    return False
 
 
def compact():
    items = [x for x in inventory if x != "Empty"]
    items += ["Empty"] * (SIZE - len(items))
    for i in range(SIZE):
        inventory[i] = items[i]
 
 
if __name__ == "__main__":
    add_item("Меч")
    add_item("Щит")
    add_item("Зілля")
    print(inventory)
 
    remove_item("Щит")
    print(inventory)
 
    add_item("Лук")
    add_item("Шолом")
    print(inventory)
 
    remove_item("Меч")
    print(inventory)
 
    compact()
    print(inventory)
 
