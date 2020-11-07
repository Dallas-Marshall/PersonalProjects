class Shop:
    """Shop class to represent details of a store."""

    def __init__(self, name="", location_x=0, location_y="", description="", inventory=None):
        """Initialise a Store."""
        if inventory is None:
            inventory = []
        self.name = name
        self.location_x = location_x
        self.location_y = location_y
        self.description = description
        self.inventory = inventory

    def __str__(self):
        """Return a string representation of a Store."""
        return "{self.name} - {self.description} ({self.location_x},{self.location_y})".format(self=self)

    def update_description(self, new_description):
        """Update a Stores Description."""
        self.description = new_description

    def update_location(self, location_x, location_y):
        """Update a Stores location."""
        self.location_x = location_x
        self.location_y = location_y
