letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def get_index(char):
	for i in xrange(len(letters)):
		if char==letters[i]:
			return i
def caesar(message,x):
	cipher_message=[]
	for char in message:
		new_index=(get_index(char)+x)%26
		new_char=letters[new_index]
		cipher_message.append(new_char)
	return ''.join(cipher_message)
	
def get_message():
	message=raw_input().upper()
	return message
	
print "enter plaintext:"
m=get_message()
print "enter x"
x=int(input())
print caesar(m,x)
