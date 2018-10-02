"""Python function to create a list of "access-list" for "global_access" and "fw-management_access_in"""

def access_list_1(file_name):
	file=open(file_name)
	list_1=[]
	for line in file:
		line=line.strip()
		for i in line.split():	#add that line to list_1 if line contains global-access or fw-management 
			if i=='global_var' or i=='fw-management_access_in':
				list_1.append(line)
	return list_1
print(access_list_1('running-config.cfg')		
