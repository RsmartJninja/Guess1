print "Daily Menu Prize List"

dishes = []
prizes = []

dish = raw_input("Please enter a starter: ")
dishes.append(dish)
prize = int(raw_input("Please enter the prize for the starter: "))
prizes.append(prize)
next = raw_input("Do you want to store now the main course? (yes/no)")

if next == "yes":
    dish = raw_input("Please enter a main course: ")
    dishes.append(dish)
    prize = int(raw_input("Please enter the prize for the main course: "))
    prizes.append(prize)
    next = raw_input("Do you want to store now the dessert course? (yes/no)")
if next == "no":
    print "Menue of Today " "%s" "for only" "%s"  % (dishes, prizes)

if next == "yes":
    dish = raw_input("Please enter a dessert: ")
    dishes.append(dish)
    prize = int(raw_input("Please enter the prize for the dessert: "))
    prizes.append(prize)
    next = raw_input("Do you want to print the Menue? (yes/no)")
if next == "yes":
    print "Menue of Today " "%s" "for only" "%s"  % (dishes, prizes)
if next == "no":
    print "Goodbye!"

with open("menu.txt", "w+") as menu_file:
    menu_file.write ("Daily dishes:\n")
    menu_file.write("- " + str(dishes) + "\n")
    menu_file.write("\n")
    menu_file.write ("Daily prizes:\n")
    menu_file.write ("- " + str(prizes) + "\n")










