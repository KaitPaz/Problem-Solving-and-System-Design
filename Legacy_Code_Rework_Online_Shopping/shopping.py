from cart import Cart
from product_catalog import ProductCatalog

def get_integer_input(prompt):
    """Gets an integer input from the user with error handling."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def handle_view_cart(cart):
    """Handles the 'View Cart' option."""
    print(cart)

def handle_browse_catalog(cart, catalog):
    """Handles the 'Browse Product Catalog' option."""
    while True:
        print(catalog)
        print("1. Add Item to Cart")
        #New option: remove item from cart
        print("2. Remove Item from Cart")
        #New option: clear cart
        print("3. Clear cart")
        print("4. Return to Main Menu")
        catalog_choice = input("Enter your choice (1, 2, 3 or 4): ")
        if catalog_choice == "1":
            product_name = input("Enter product name to add to cart: ")
            try:
                cart.add_product(product_name)
                print(f"Added {product_name} to cart.")
            except ValueError as e:
                print(e)

        #New option (remove_product)  implemented
        elif catalog_choice == "2":
            if not cart.products:
                print("Your cart is empty. Please add products before trying to remove them.")
                continue

            product_name = input("Enter product name to remove from cart: ")
            if product_name in cart.products:
                cart.remove_product(product_name)
                print(f"Removed {product_name} from cart.")
            else:
                print(f"{product_name} is not in your cart.")

        elif catalog_choice == "3":
            if not cart.products:
                print("Your cart is already empty.")
            else:
                cart.clear_cart()
                print("Your cart has been cleared.")


        elif catalog_choice == "4":
            break

       

        else:
            print("Invalid choice.")

        

def handle_checkout(cart):
    """Handles the 'Checkout' option."""
    if len(cart.products) == 0:
        print("\n\nCome back again soon!\n")

    else:
        print(cart)
        print("Thank you for your order!")
       


def run_interactive_simulation():
    """Runs the interactive shopping cart simulation."""
    catalog = ProductCatalog()
    catalog.add_product("Laptop", 800.0)
    catalog.add_product("Mouse", 40.0)
    catalog.add_product("Keyboard", 80.0 )
    catalog.add_product("Monitor", 400.0)
    catalog.add_product("USB Drive",15.0 )

    cart = Cart(catalog)

    while True:
        print("\n--- Main Menu ---")
        print("1. Browse Product Catalog")
        print("2. View Cart")
        print("3. Checkout")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            handle_browse_catalog(cart, catalog)
        elif choice == "2":
            handle_view_cart(cart)
        elif choice == "3":
            handle_checkout(cart)
            return
        else:
            print("Invalid choice.")

# --- Main program ---
if __name__ == "__main__":
    run_interactive_simulation()
