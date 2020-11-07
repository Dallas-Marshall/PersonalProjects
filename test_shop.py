from Inventory import Inventory
from Item import Item
from shop import Shop


def run_tests():
    """Test Shop class."""

    # Create Inventory
    item1 = Item("Blue Wool", "2 Stacks", 1)
    item2 = Item("Red Wool", "2 Stacks", 1)
    inv = Inventory()
    inv.add_item(item1)
    inv.add_item(item2)

    # Create Shop
    shop = Shop("All Australian Wool", 300, 400, "All your wool Needs!", inv)
    print(shop)

    # Test update_description
    shop.update_description("Lots of wool Colours")
    print(shop)

    # Test update Location
    shop.update_location(509, 5002)
    print(shop)

    # Test list Inventory
    for item in shop.inventory.items:
        print(item)


run_tests()
