
    """Manages a collection of products."""

    def __init__(self):
        self.products = {} #Changed from set to dictionary to incorporate prices

    def add_product(self, product, price): #Change: Added price argument
        """Adds a product to the catalog."""
       # self.products.add(product)
        if product in self.products:
            raise ValueError("Product already exists")
        self.products[product] = price

    #New function
    def get_price(self, product):
        """
        Returns the price of a product
        """
        return float(self.products[product])

    def __str__(self):
        """Returns a string representation of all products in the catalog."""
        output = "\n--- Product Catalog ---\n"
        if not self.products:
            output += "No products in catalog.\n"
        else:
            for product in sorted(self.products):
                price = self.get_price(product)
                output += f"{product:<15} ${price:>6.2f}\n"
        output += "---------------------\n"
        return output

    def __contains__(self, product):
        """Checks if a product exists in the catalog."""
        return product in self.products



