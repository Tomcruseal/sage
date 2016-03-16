import numpy
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
K=Matrix([[3,2],[1,1]])
plaintext=raw_input().upper()

def indexOfString(plaintext):
	indexes=[]
	for char in plaintext:
		for j in xrange(len(letters)):
			if char==letters[j]:
				indexes.append(j)
	return indexes
indexes=indexOfString(plaintext)
cipher_indexes=[]
cipher_indexes2=[]
for i in xrange(len(indexes)):
	new_matrix=Matrix([i,i+1])
	temp=numpy.ravel(new_matrix*K%26)
	cipher_indexes.append(temp.tolist())
	
print type(cipher_indexes)
print cipher_indexes
new_L=sum(cipher_indexes,[])
print new_L
#print type(cipher_indexes2)
#print cipher_indexes2
cipher_text=[]
for i in new_L:
	cipher_text.append(letters[int(i)])
print (cipher_text)
m=''.join(cipher_text)	
print m

