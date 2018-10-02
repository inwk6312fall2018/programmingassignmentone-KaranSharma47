"""Write a Python function to create a new configuration file that 
replaces all (sub-)interface IP addresses that start with '172.' and '192." to "10." 
and also change the security-level to "10"  """

def change_ip(file_name):
	file=open(file_name)
	list_1=[]
	list_12=[]	# all ip addresses
	list_13=[]	#all list of elements in ip add
	list_14=[]	#updated ip list 
	for line in file:
		line=line.strip()
		for word in line.split():
			list_1.append(word)
	for i in range(len(list_1)):
		if list_1[i-1]!='no' and list_1[i]=='ip' and list_1[i+1]=='address':
			list_12.append(list_1[i+2])	# all ip add in list_12
	for i in list_12:
		list_13.append(i.split('.'))	#list of elements in ip
	for i in list_13:		#delete '172' or '192' and update with '10'
		del i[0]	#delete first element
		i.insert(0,'10')	
		list_14.append('.'.join(i))	
	return list_14

print(change_ip('running-config.txt'))
