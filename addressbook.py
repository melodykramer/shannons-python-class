
#creates an empty list for each quadrant in DC

nw_addresses = []
sw_addresses = []
ne_addresses = []
se_addresses = []

#asks someone for three addresses

for x in range(3):

	address = raw_input ("Type in your address ")

#splits each address into a list

	addresssplit = address.split(" ") 


#prints out each address

	print address
	
#if an item is in a certain quadrant, add that item to a list 


	if 'NW' in address or 'nw' in address:
		nw_addresses.append(address)
	if 'NE' in or 'ne' in address:
		ne_addresses.append(address)
	if 'SW' in address:
		sw_addresses.append(address)
	if 'SE' in address:
		se_addresses.append(address)

#print out your quadrants

print ("Here are your NW addresses")
print nw_addresses
print ("Here are your NE addresses")
print ne_addresses
print ("Here are your SW addresses")
print sw_addresses
print ("Here are your SE addresses")
print se_addresses
