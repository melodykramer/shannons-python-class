contacts = {}

contacts = {

'Shannon': {'phone':'202-123-5555', 'twitter':'@svt827', 'github': '@shannonturner'},

'Anupama': {'phone': '234-234-2343', 'twitter': '@iamtheanupama', 'github': "@asdfsadf"}

}



for contact in sorted(contacts.keys()):
	print contact + '\'s contact information is'
	print 'Phone:' + contacts[contact]['phone']
	print 'Twitter:' + contacts[contact]['twitter']
	print 'Github:' + contacts[contact]['github']
