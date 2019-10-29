
#ask user total meal price and service score
meal_price = float (raw_input ("What was the total price of your meal?: $ "))
serv_score = int (raw_input ("How was the service on a scale from 1-10?: "))

#funny program commentary
if serv_score >= 8:
    print ("That is some great service!")
elif serv_score >=6:
    print ("They could have done better but not too bad...")
elif serv_score < 6:
    print ("They need to work on their service XP")

#find total price with tip included
if serv_score == 10:
    print (("Total service tip is $" + ("%.2f" %(meal_price *.25)) + " and total price with tip is $") +( "%.2f" %((meal_price *.25) + meal_price)))
elif serv_score >= 8:
    print (("Total service tip is $" + ("%.2f" %(meal_price *.2)) + " and total price with tip is $") +( "%.2f" %((meal_price *.2) + meal_price)))
elif serv_score >= 6:
    print (("Total service tip is $" + ("%.2f" %(meal_price *.15)) + " and total price with tip is $") +( "%.2f" %((meal_price *.15) + meal_price)))
elif serv_score >= 4:
    print (("Total service tip is $" + ("%.2f" %(meal_price *.13)) + " and total price with tip is $") +( "%.2f" %((meal_price *.13) + meal_price)))
elif serv_score >= 1:
    print (("Total service tip is $" + ("%.2f" %(meal_price *.1)) + " and total price with tip is $") +( "%.2f" %((meal_price *.10) + meal_price)))
