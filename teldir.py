def print_menu():
    print('1. Add a Phone Number')
    print('2. search a Phone Number')
    print('3. Quit')
    print()

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 3:
    menu_choice = int(input("Type in a number (1-3): "))
    if menu_choice == 1:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone)
    elif menu_choice == 2:
        print("search Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice != 3:
        print_menu()

