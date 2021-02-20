from Inventory import Inventory
from Item import Item
from store import Store


def run_tests():
    """Test Store class."""

    # Create Inventory
    item1 = Item("Blue Wool", "2 Stacks", 1)
    item2 = Item("Red Wool", "2 Stacks", 1)
    inv = Inventory()
    inv.add_item(item1)
    inv.add_item(item2)

    # Create Store
    store = Store("All Australian Wool", 300, 400, "All your wool Needs!", inv)
    print(store)

    # Test update_description
    store.update_description("Lots of wool Colours")
    print(store)

    # Test update Location
    store.update_location(509, 5002)
    print(store)

    # Test list Inventory
    for item in store.inventory.items:
        print(item)


run_tests()
