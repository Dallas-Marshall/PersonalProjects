class Item:
    """Item class to represent details of an Item object."""

    def __init__(self, name="", quantity="", cost=0):
        """Initialise a Store."""
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def __str__(self):
        """Return a string representation of an Item."""
        return "{self.name} - {self.quantity} / {self.cost}D".format(self=self)

    def update_quantity(self, new_quantity):
        """Update a Stores Description."""
        self.quantity = new_quantity

    def update_cost(self, new_cost):
        """Update a Stores location."""
        self.cost = new_cost
