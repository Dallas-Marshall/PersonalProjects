from Item import Item


def run_tests():
    """Test Item class."""

    # Create Item
    item = Item("Blue Wool", "2 Stacks", 1)
    print(item)

    # Test update_description
    item.update_cost(2)
    print(item)

    # Test update Location
    item.update_quantity(16)
    print(item)


run_tests()
