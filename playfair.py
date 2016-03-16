letters=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']	#25 letters without J
def get_key():						#modify the key
	element=raw_input().upper()
	key=[]
	for char in element:
		if char in letters and char not in key:
			key.append(char)
		elif char == 'J':
			key.append('I')			#replace 'J' with 'I'
	for char in letters:
		if char not in key:
			key.append(char)		#reinforce remainning space with the letters			
	return key

def gen_matrix(key):								#generate the matrix
	matrix=[]
	counter=0
	for x_count in xrange(5):
		x=[]
		for y_count in xrange(5):
			x.append(key[counter])
			counter+=1
		matrix.append(x)
	return matrix
	
def print_matrix(matrix):							#print the key matrix
	for counter in xrange(5):
		print "%c %c %c %c %c" % (matrix[counter][0],matrix[counter][1],matrix[counter][2],matrix[counter][3],matrix[counter][4])
		print "\n"

def get_message():									#modify the original message
	ori_message=raw_input()
	mod_message=[]
	for char in ori_message.upper():
		if char in letters:
			mod_message.append(char)
		elif char == 'J':
			mod_message.append('I')
	return ''.join(mod_message)		


def get_coordinate(substring,matrix):				#get the coordinates of certain substring 
	coordinate=[]
	for char in substring:
		for x in xrange(5):
			for y in xrange(5):
				if char == matrix[x][y]:
					coordinate.append((x,y))
	return coordinate

def parse_message(message):							#slice the modified message
	substrings=[]
	while len(message)>0:
		substring=message[:2]
		if len(substring)==1:						#add a 'X' to the end of a single character
			substring="%c%c" % (substring[0],'X')
			substrinfs.append(substring)
			message=message[1:]
		elif substring[0]==substring[1]:
			substring="%c%c" % (substring[0],'X')
			substrings.append(substring)
			message=message[1:]
		else:
			substrings.append(substring)
			message=message[2:]
	return substrings

def encrypt(message,matrix):							#function for encrypt the plaintext
	coordinates=[]
	ciphertext=[]
	substrings=parse_message(message)
	for s in substrings:
		temp=[]
		coordinates=get_coordinate(s,matrix)
		if coordinates[0][0]==coordinates[1][0]:
			(x0,y0)=(coordinates[0][0],(coordinates[0][1]+1)%5)
			temp.append(matrix[x0][y0])
			(x1,y1)=(coordinates[1][0],(coordinates[1][1]+1)%5)
			temp.append(matrix[x1][y1])
		elif coordinates[0][1]==coordinates[1][1]:
			(x0,y0)=((coordinates[0][0]+1)%5,coordinates[0][1])
			temp.append(matrix[x0][y0])
			(x1,y1)=((coordinates[1][0]+1)%5,coordinates[1][1])
			temp.append(matrix[x1][y1])
		else: 
			(x0,y0)=(coordinates[0][0],coordinates[1][1])
			temp.append(matrix[x0][y0])
			(x1,y1)=(coordinates[1][0],coordinates[0][1])
			temp.append(matrix[x1][y1])
		ciphertext.append(''.join(temp))
	print ciphertext
	print "encrpyted message: %s " % ''.join(ciphertext)			
	
def decrypt(message,matrix):							#function for decrypt the ciphertext
	coordinates=[]
	plaintext=[]
	substrings=parse_message(message)
	for s in substrings:
		temp=[]
		coordinates=get_coordinate(s,matrix)
		if coordinates[0][0]==coordinates[1][0]:
			(x0,y0)=(coordinates[0][0],(coordinates[0][1]-1)%5)
			temp.append(matrix[x0][y0])
			(x1,y1)=(coordinates[1][0],(coordinates[1][1]-1)%5)
			temp.append(matrix[x1][y1])
		elif coordinates[0][1]==coordinates[1][1]:
			(x0,y0)=((coordinates[0][0]-1)%5,coordinates[0][1])
			temp.append(matrix[x0][y0])
			(x1,y1)=((coordinates[1][0]-1)%5,coordinates[1][1])
			temp.append(matrix[x1][y1])
		else:
			(x0,y0)=(coordinates[0][0],coordinates[1][1])
			temp.append(matrix[x0][y0])
			(x1,y1)=(coordinates[1][0],coordinates[0][1])
			temp.append(matrix[x1][y1])
		plaintext.append(''.join(temp))
	print "decrpted message: %s" % ''.join(plaintext)		

print "enter the keys"
thekeys=get_key()
thematrix=gen_matrix(thekeys)
print "the matrix is "
print print_matrix(thematrix)
#print "enter the plaintext:"
print "enter the ciphertext:"
themessage=get_message()
substrings=parse_message(themessage)
print substrings
#encrypt(themessage,thematrix)
decrypt(themessage,thematrix)











	









	
