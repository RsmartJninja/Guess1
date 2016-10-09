#Friendly Converter

do_it_again= True

while do_it_again:
    kilo = int(raw_input ("Hi, do you fancy converting kilometers in miles? Type kilometers & enter:"))
    miles = kilo *0.6213711922;
    print str(kilo) + " kilometers are " + str(miles) + " miles."
    repeat_it = raw_input("Do you want to make another conversion (yes|no) ")
    do_it_again = False
    while repeat_it == "yes":
        kilo = int(raw_input("Type kilometers & enter:"))
        miles = kilo * 0.6213711922;
        print str(kilo) + " kilometers are " + str(miles) + " miles."
        repeat_it = raw_input("Do you want to make another conversion (yes|no) ")
    if repeat_it == "no":
        print "Good bye!"