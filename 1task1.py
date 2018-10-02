"" This function will give list that contains tuple""
def int_and_int_name(file_name):
	file=open(file_name)
	list_1=[]
	list_2=[]	#INTERFACE 
	list_3=[]	#INTERFACE NAME
	list_4=[]	#TUPLE (interface,interface name)
	for line in file:
		line=line.strip()
		for word in line.split():
			list_1.append(word)	# WILL MAKE A LIST OF ALL WORDS
	for i in range(len(list_1)):
		if list_1[i]=='interface':
			list_2.append(list_1[i+1])	#MAKE LIST OF INTERFACE
		elif list_1[i]=='nameif' or (list_1[i]=='no' and list_1[i+1]=='nameif'):
			#MAKE LIST OF INTERFACE NAME AS WELL
			if list_1[i]=='no' and list_1[i+1]=='nameif':
				list_3.append('no name')
			elif list_1[i-1]!='no' and list_1[i]=='nameif':
				list_3.append(list_1[i+1])
	for i in range(len(list_2)):			#CREATE LIST OF TUPLE(INTERFACE,INTERFACE NAME)
		list_4.append((list_2[i],list_3[i]))
	return list_4



def list_ifname_ip(file_name):
	file=open(file_name)
	list_1=[]
	list_2=[]	#INTERFACE LIST
	list_3=[]	#NAME OF INTERFACE
	list_4=[]	#VLAN ID
	list_5=[]	# IP ADDRESS
	list_6=[]	#SUBNETMASK
	list_7=[]	#LIST OF INTERFACE NAME,VLANID,IP ADDRESS,SUBNETMASK
	dict={}	#DICTIONARY
	for line in file:
		line=line.strip()
		for word in line.split():
			list_1.append(word)
	for i in range(len(list_1)):
		if list_1[i]=='interface':
			list_2.append(list_1[i+1])  #MAKING LIST OF INTERFACE
		elif list_1[i]=='nameif' or (list_1[i]=='no' and list_1[i+1]=='nameif'):
			#MAKING A LIST OF INTERFACE NAME
			if list_1[i]=='no' and list_1[i+1]=='nameif':
				list_3.append('no name')
				list_4.append('no vlan')	#FOR THE INTERFACE WHICH HAS NO NAME , NO IP ADDRESS AND NO SUBNETMASK
				list_5.append('no ip address')
				list_6.append('no netmask')
			elif list_1[i-1]!='no' and list_1[i]=='nameif':
				list_3.append(list_1[i+1])
				list_5.append(list_1[i+6])
				list_6.append(list_1[i+7])
				if list_1[i-1]=='management-only':	# MANAGEMENT NETWORK CAS
					list_4.append('no vlan')
				else:
					list_4.append(list_1[i-2]+list_1[i-1])
	for i in range(len(list_2)):
		list_7=[]
		list_7.append(list_3[i])
		list_7.append(list_4[i])
		list_7.append(list_5[i])
		list_7.append(list_6[i])
		dict[list_2[i]]=list_7	#add list of nameif,ip,netMask as value in dict
	return dict


print('List contain tuple interface (interfacename,"nameif"- value) is:\n',int_and_int_name('running-config.cfg'))
print('dictionary that contains the "interfacename" as the key and "nameif,VLAN,IPaddress,NetMask" list as the value is :\n',list_ifname_ip('running-config.cfg'))
