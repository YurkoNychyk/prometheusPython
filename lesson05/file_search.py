#Lesson05: file search
def file_search(folder, filename):
	path = folder[0] + "/"
	current_item = 1
	
	if len (folder) > 1:

		while current_item < len(folder):
			if type(folder[current_item]) == str:
				if folder[current_item] == filename:
					return path + folder[current_item]
				#print "fiound file " + path + folder[current_item]
			else:
				if file_search(folder[current_item], filename) != None:
					if file_search(folder[current_item], filename) != False:
						return path + file_search(folder[current_item], filename)
				
			current_item += 1
		return False
	else:
		return False



	# path = folder[0]
	# if type(folder) == list:
	# 	if len(folder) > 1:
	# 		print
	# 		print "Openinig folder " + folder[0] + " containing " + str(len(folder)-1) + " items:"
	# 		current_folder_item = 0
			
	# 		while current_folder_item < len (folder):
	# 			print "Element " + str(current_folder_item) + ": " + str(folder[current_folder_item])
	# 			file_search(folder[current_folder_item], filename) 	
	# 			current_folder_item += 1
	# else:
	# 	print
	# 	print "Checking file " + folder
	# 	if folder == filename:
	# 		return folder	
			
			

