class Cart:
    """Represents a shopping cart with a set of products."""

    def __init__(self, catalog):
        self.products = {}
        self.catalog = catalog

    def add_product(self, product):
        """Adds a product to the cart.

        Raises:
            ValueError: If the product is already in the cart.
            KeyError: If the product is not in the catalog.
        """

        #These lines of code caused the quantity error therfore are commented out
        #if product in self.products:
           # raise ValueError(f"Product {product} already added to cart!")
        if product not in self.catalog:
            # Changed to key error for more precision
            raise KeyError(f"Product {product} not in catalog!")

        # Increments count of products in the Cart
        if product in self.products:
            self.products[product] += 1

        else:
            self.products[product] = 1

    #New function
    def remove_product(self, product):
        """
        Removes a product from the cart
        """
        count = self.products.get(product, 0)

        if count == 0:
            raise KeyError(f"No products can be removed if cart is empty")
        if count > 1:
            self.products[product] = count - 1
        elif count == 1:
            del self.products[product]

    #New function
    def clear_cart(self):
        """
        Clear the cart of all its products
        """

        self.products.clear()


    def __str__(self):
        """Returns a string representation of the cart's contents."""
        output = "\n--- Your Cart ---\n"
        total = 0.0
        if not self.products:
            output += "\nYour cart is empty.\n"
        else:
            for product in sorted(self.products):
                #Change: display quantity
                quantity = self.products[product]
                price = self.catalog.get_price(product)

                
                if quantity == 1:
                    output += f"- {product} (x{quantity}) (${price})\n"
                    total += price
                if quantity >1 :
                    price = price * quantity
                    output += f"- {product} (x{quantity}) (${price})\n"
                    total += price
        

        output += f"Total: ${total}\n"
        return output

    def __contains__(self, product):
        """Checks if a product is in the cart."""
        return product in self.products
