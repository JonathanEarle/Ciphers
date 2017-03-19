#Can be replaced by any search function
def linSearch(p,list):
	for i in range(0,len(list)):
		if(list[i]==p):
			return i
	return -1

#Encrypt
def encrypt(message,pos,sortedPos,length):
	encrypted=""
	for i in range(0,length):
		p=sortedPos[i]
		res=linSearch(p,pos)
		if(res>-1):#Unecessary condition
			encrypted+=message[res]
	return encrypted

#Decrypt
def decrypt(encrypted,pos,sortedPos,length):
	decrypted=""
	for i in range(0,length):
		p=pos[i]
		res=linSearch(p,sortedPos)
		if(res>-1):
			decrypted+=encrypted[res]
	return decrypted

def main():
	message="hello"
	rail=3
	length=len(message)

	pos=[]
	i=0
	j=0
	sign=-1
	for k in range(0,length):
		if(i==rail-1 or i==0):
			sign=sign*-1
		pos.append((i,j))
		j=j+1
		i=i+sign
	sortedPos=sorted(pos)

	#Prints and stores the encrypted message
	encrypted=encrypt(message,pos,sortedPos,length)
	print(encrypted)

	decrypted=decrypt(encrypted,pos,sortedPos,length)
	print(decrypted)
	
if __name__=="__main__":
	main()
