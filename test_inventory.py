from Inventory import Inventory
from Item import Item


def run_tests():
    """Test Inventory class."""

    # Test empty Inventory (defaults)
    print("Test empty Inventory:")
    inv = Inventory()
    assert not inv.items  # an empty list is considered False

    # Test adding an Item with values
    print("\nTest adding Item:")
    inv.add_item(Item("Red Wool", "2 Stacks", 2))
    inv.add_item(Item("Green Wool", "2 Stacks", 2))

    # Test list_inventory
    for item in inv.list_items():
        print(item)


run_tests()
