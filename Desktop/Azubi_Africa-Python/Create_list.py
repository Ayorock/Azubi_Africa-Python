list_item = []

while True:
    print("\n1. Add item to List")
    print("2. Remove item from List")
    print("3. View List")
    print("4. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter the name of the item: ")
        list_item.append(name)
           
    elif choice == "2":
        name = input("Enter the name of the item to remove: ")
        list_item.remove(name)

    elif choice == "3":
        print(list_item)
            
    elif choice == "4":
        print("Exiting the shopping cart application. Goodbye!")
        break

else:
    print("Invalid choice. Please enter a number between 1 and 5.")


