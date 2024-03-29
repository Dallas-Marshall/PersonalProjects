from catalogue import Catalogue
from store import Store


def run_tests():
    """Test Catalogue class."""

    # Test empty Catalogue (defaults)
    print("Test empty Catalogue:")
    catalogue = Catalogue()
    assert not catalogue.stores  # an empty list is considered False

    # Test loading stores
    print("\nTest loading Stores:")
    catalogue.load_stores('store_saves.csv')

    for shop in catalogue.list_stores():
        print(f'\n{shop}')

        print("\nTest listing shop inventory")
        for item in shop.inventory.list_items():
            print(item)
    assert catalogue.stores  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Shop with values
    print("\nTest adding new Shop:")
    catalogue.add_store(Store("Squelons Wood", 300, 500, "I sell wood!"))
    for shop in catalogue.list_stores():
        print(shop)

    # Test saving Stores (check CSV file manually to see results)
    catalogue.save_stores('test.csv')


run_tests()
