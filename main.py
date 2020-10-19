print("Change Calclator")

quarter = 25
dime = 10
nickel = 5
penny = 1

moneygiven = input("Enter how much money given: ")
citem = input("How much did the item cost?: ")

#Write your code here to give exact number of quarters (qmb) and dimes (dmb) and nickels (nmb) and pennies (pnb) 
#based on the difference between citem (how much the time cost) and moneygiven (how much you paid with)

# First Draft
mg = float(moneygiven)
ci = float(citem)
change = mg - ci

qmb = int(change/.25)
change = change - qmb*.25
dmb = int(change/.10)
change = change - dmb*.10
nmb = int(change/.5)
change = change - nmb*.5
pmb = int(change/.01)
change = change - pmb*.01



print("You need {0} quarters, {1} dimes, {2} nickels, {3} pennies.".format(qmb, dmb, nmb, pmb))