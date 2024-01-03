class ShoppingCart:
    def __init__(self):
        self.shopping_cart = []

    def add_item(self, name, price):
        self.shopping_cart.append({"name": name, "price": price})
        print(f"{name} added to the shopping cart.")

    def remove_item(self, name):
        for item in self.shopping_cart:
            if item["name"].lower() == name.lower():
                self.shopping_cart.remove(item)
                print(f"{name} removed from the shopping cart.")
                return
        print(f"{name} not found in the shopping cart.")

    def view_cart(self):
        print("Shopping Cart:")
        for item in self.shopping_cart:
            print(f"{item['name']}: ${item['price']}")

    def calculate_total(self):
        total = sum(item["price"] for item in self.shopping_cart)
        print(f"Total cost: ${total}")


def main():
    shopping_cart = ShoppingCart()

    while True:
        print("\n1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Calculate total")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter the name of the item: ")
            price = float(input("Enter the price of the item: "))
            shopping_cart.add_item(name, price)

        elif choice == "2":
            name = input("Enter the name of the item to remove: ")
            shopping_cart.remove_item(name)

        elif choice == "3":
            shopping_cart.view_cart()

        elif choice == "4":
            shopping_cart.calculate_total()

        elif choice == "5":
            print("Exiting the shopping cart application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
