letters=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def getKey():
	element=raw_input().upper()
	key=[]
	for char in element:
		if char in letters and char not in key:
			key.append(char)
		elif char is 'J':
			key.append('I')			#replace 'J' with 'I'
	for char in letters:
		if char not in key:
			key.append(char)		#reinforce remainning space with the letters			
	
