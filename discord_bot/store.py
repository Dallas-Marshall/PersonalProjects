class Store:
    """Shop class to represent details of a store."""

    def __init__(self, name="", location_x=0, location_z=0, description="", inventory=None):
        """Initialise a Store."""
        if inventory is None:
            inventory = []
        self.name = name
        self.location_x = location_x
        self.location_z = location_z
        self.description = description
        self.inventory = inventory

    def __str__(self):
        """Return a string representation of a Store."""
        return "{self.name} - {self.description} ({self.location_x},{self.location_y})".format(self=self)

    def update_description(self, new_description):
        """Update a Stores Description."""
        self.description = new_description

    def update_location(self, location_x, location_z):
        """Update a Stores location."""
        self.location_x = location_x
        self.location_z = location_z
