# Python Program for List, Tuple, Set, and Dictionary Operations

my_list = []
my_set = set()
my_dict = {}

while True:
    print("\n===== MENU =====")
    print("1. List Operations")
    print("2. Tuple Operations")
    print("3. Set Operations")
    print("4. Dictionary Operations")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # LIST OPERATIONS
    if choice == 1:
        while True:
            print("\n--- LIST OPERATIONS ---")
            print("1. Insert")
            print("2. Update")
            print("3. Delete")
            print("4. Display")
            print("5. Sort")
            print("6. Search")
            print("7. Back")

            ch = int(input("Enter choice: "))

            if ch == 1:
                item = input("Enter item: ")
                my_list.append(item)
                print("Inserted Successfully")

            elif ch == 2:
                old = input("Enter item to update: ")
                if old in my_list:
                    new = input("Enter new value: ")
                    idx = my_list.index(old)
                    my_list[idx] = new
                    print("Updated Successfully")
                else:
                    print("Item not found")

            elif ch == 3:
                item = input("Enter item to delete: ")
                if item in my_list:
                    my_list.remove(item)
                    print("Deleted Successfully")
                else:
                    print("Item not found")

            elif ch == 4:
                print("List:", my_list)

            elif ch == 5:
                my_list.sort()
                print("Sorted List:", my_list)

            elif ch == 6:
                item = input("Enter item to search: ")
                if item in my_list:
                    print("Item Found")
                else:
                    print("Item Not Found")

            elif ch == 7:
                break

    # TUPLE OPERATIONS
    elif choice == 2:
        print("\n--- TUPLE OPERATIONS ---")
        tup = tuple(input("Enter tuple elements separated by space: ").split())
        print("Tuple:", tup)

        key = input("Enter element to search: ")
        if key in tup:
            print("Element Found")
        else:
            print("Element Not Found")

        print("Sorted Tuple:", tuple(sorted(tup)))

    # SET OPERATIONS
    elif choice == 3:
        while True:
            print("\n--- SET OPERATIONS ---")
            print("1. Insert")
            print("2. Delete")
            print("3. Display")
            print("4. Search")
            print("5. Back")

            ch = int(input("Enter choice: "))

            if ch == 1:
                item = input("Enter item: ")
                my_set.add(item)
                print("Inserted Successfully")

            elif ch == 2:
                item = input("Enter item to delete: ")
                if item in my_set:
                    my_set.remove(item)
                    print("Deleted Successfully")
                else:
                    print("Item not found")

            elif ch == 3:
                print("Set:", my_set)

            elif ch == 4:
                item = input("Enter item to search: ")
                if item in my_set:
                    print("Item Found")
                else:
                    print("Item Not Found")

            elif ch == 5:
                break

    # DICTIONARY OPERATIONS
    elif choice == 4:
        while True:
            print("\n--- DICTIONARY OPERATIONS ---")
            print("1. Insert")
            print("2. Update")
            print("3. Delete")
            print("4. Display")
            print("5. Search")
            print("6. Back")

            ch = int(input("Enter choice: "))

            if ch == 1:
                key = input("Enter key: ")
                value = input("Enter value: ")
                my_dict[key] = value
                print("Inserted Successfully")

            elif ch == 2:
                key = input("Enter key to update: ")
                if key in my_dict:
                    value = input("Enter new value: ")
                    my_dict[key] = value
                    print("Updated Successfully")
                else:
                    print("Key not found")

            elif ch == 3:
                key = input("Enter key to delete: ")
                if key in my_dict:
                    del my_dict[key]
                    print("Deleted Successfully")
                else:
                    print("Key not found")

            elif ch == 4:
                print("Dictionary:", my_dict)

            elif ch == 5:
                key = input("Enter key to search: ")
                if key in my_dict:
                    print("Value =", my_dict[key])
                else:
                    print("Key not found")

            elif ch == 6:
                break

    # EXIT
    elif choice == 5:
        print("Program Terminated")
        break

    else:
        print("Invalid Choice")
