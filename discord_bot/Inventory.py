class Inventory:
    """Inventory class to keep track of a list of Item objects."""

    def __init__(self):
        """Initialise an Inventory."""
        self.items = []

    def __len__(self):
        """Return number of Store objects."""
        return len(self.items)

    def list_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        """Remove an Item from the list of items.
        :returns boolean: True if item is successfully removed.
        """
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return True
