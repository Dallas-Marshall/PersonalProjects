from Inventory import Inventory
from Item import Item
from store import Store

INDEX_OF_NAME = 0
INDEX_OF_LOCATION_X = 1
INDEX_OF_LOCATION_Z = 2
INDEX_OF_DESCRIPTION = 3
INDEX_OF_ITEMS = 4

INDEX_OF_ITEM_NAME = 0
INDEX_OF_ITEM_QUANTITY = 1
INDEX_OF_ITEM_COST = 2


class Catalogue:
    """Catalogue class to keep track of a list of Store objects."""

    def __init__(self):
        """Initialise empty list to track Store objects."""
        self.stores = []

    def __len__(self):
        """Return number of Store objects."""
        return len(self.stores)

    def list_stores(self):
        """Returns list of stores."""
        return self.stores

    def add_store(self, store):
        """Add a Store to the list of stores."""
        self.stores.append(store)

    def remove_store(self, store_name):
        """Remove a Store from the list of stores if it exists.
        :returns boolean: True if store is successfully removed.
        """
        for store in self.stores:
            if store.name.lower() == store_name.lower():
                self.stores.remove(store)
                return True

    def load_stores(self, path_to_file):
        """Read the file containing Stores and add to list."""

        # Read file
        in_file = open(path_to_file, 'r')
        for line in in_file:
            line_str = line.strip().split(',')

            # Create Inventory
            shop_inventory = Inventory()

            # Separate Items
            items = line_str[INDEX_OF_ITEMS].strip().split('-')
            if items != ['']:
                for item in items:
                    details = item.strip().split('|')
                    # Create Item Objects
                    item_name = details[INDEX_OF_ITEM_NAME]
                    item_quantity = details[INDEX_OF_ITEM_QUANTITY]
                    item_cost = int(details[INDEX_OF_ITEM_COST])

                    item_object = Item(item_name, item_quantity, item_cost)

                    # Add to Inventory
                    shop_inventory.add_item(item_object)

            # Create Shop
            shop_name = line_str[INDEX_OF_NAME]
            shop_location_x = line_str[INDEX_OF_LOCATION_X]
            shop_location_z = line_str[INDEX_OF_LOCATION_Z]
            shop_description = line_str[INDEX_OF_DESCRIPTION]

            shop = Store(shop_name, shop_location_x, shop_location_z, shop_description, shop_inventory)
            self.stores.append(shop)
        in_file.close()

    def save_stores(self, path_to_file):
        """Save Stores to file."""
        out_file = open(path_to_file, 'w')
        for shop in self.stores:
            out_file.write(f'{shop.name},{shop.location_x},{shop.location_z},{shop.description},')

            if len(shop.inventory) == 0:
                out_file.write('\n')

            for i in range(0, len(shop.inventory)):
                shop_inventory = shop.inventory.list_items()
                name = shop_inventory[i].name
                quantity = shop_inventory[i].quantity
                cost = shop_inventory[i].cost
                out_file.write(f"{name}|{quantity}|{cost}")
                if i < (len(shop.inventory) - 1):
                    out_file.write('-')
                else:
                    out_file.write('\n')
        out_file.close()
