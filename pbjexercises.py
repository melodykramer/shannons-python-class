# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make

# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.


#creates variables for amount of bread, peanut butter, and jelly respectively

b = input("Enter the slices of bread you have.")
p = input("Enter the amount of peanut butter you have.")
j = input("Enter the amount of jelly you have.")


#Can I make a peanut butter and jelly sandwich? Yes, if I have at least 2 slices of bread, one sandwich-worth of pb
# and one sandwich worth of jelly.

if b>=2 and p>=1 and j>=1:
	print "You have enough to make at least one sandwich."
else:
	print "Looks like I don't have a lunch today!" 
	

#How many sandwiches can I make? We start off with zero sandwiches. As long as bread is greater than two and pb&j are greater than one, we can make a sandwich.
#When we don't have enough bread, peanut butter or jelly -- we can't make any more sandwiches!


#Also: Can I make an open faced sandwich?
	
sandwich = 0


while b >= 2 and j >=1 and p>=1:
	b = b - 2
	j = j - 1
	p = p - 1
	sandwich = sandwich + 1
	if b % 2 == 1 and j % 2 == 1 and p % 2 == 1:
		print "You can make an open face sandwich!"
print "And you can make {0} complete sandwiches!".format(sandwich)

#What ingredient did you run out of first? Run the while loop. If any of the ingredients dip, that's the missing one!

while b >= 2 and j >= 1 and p >= 1:
	b = b - 2
	j = j - 1
	p = p - 1
if b<2 and p>=1 and j>=1:
		print "You ran out of bread first!"
elif p<1 and j>1 and b>2:
		print "You ran out of peanut butter first!"
elif j<1 and p>1 and b>2:
		print "You ran out of jelly first!"

#But can I make a peanut butter sandwich?

pbsandwich=0

while b >= 2 and j >= 1 and p >= 1:
	b = b - 2
	j = j - 1
	p = p - 1
	sandwich = sandwich + 1
if j<1 and p>=1 and b>=2:
		pbsandwich = pbsandwich + 1
print "But you can make {0} peanut butter sandwiches!".format(sandwich)
