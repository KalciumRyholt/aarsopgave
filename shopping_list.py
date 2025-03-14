class ShoppingList:
    """
    A class to represent a shopping list.

    Attributes
    ----------
    items : list
        A list to store shopping items.

    Methods
    -------
    add_item(item):
        Adds an item to the shopping list.
    
    remove_item(item):
        Removes an item from the shopping list if it exists.
    
    get_items():
        Returns the list of shopping items.
    """
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
           self.items[item] += quantity
        else:
            self.items[item] = quantity



    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item] > quantity:
                self.items[item] -= quantity
            elif self.items[item] == quantity:
                del self.items[item]
            else:
                print(f"Cannot remove {quantity} {item}(s), only {self.items[item]} available")
        else:
            print(f"{item} not found in the shopping list.")

    def get_items(self):
        return self.items

# Example usage:
if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add_item("Apples",10)
    shopping_list.add_item("Bananas")
    print(shopping_list.get_items())  # Output: ['Apples', 'Bananas']
    shopping_list.remove_item("Apples")
    print(shopping_list.get_items())  # Output: ['Bananas']
