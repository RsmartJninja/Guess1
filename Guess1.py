#Guess Operator
secret = 7
guess = int(raw_input ("Guess Number:"))
print guess
if (guess==secret):  #source http://stackoverflow.com/questions/32667736/how-to-check-if-a-dictionary-value-is-equal-to-a-variables-value
    print "Congratulation!"
else:
    print "Wrong! Try it again!"



