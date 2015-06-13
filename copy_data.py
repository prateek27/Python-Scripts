import os 
import shutil 
import random 
import sys
from os import listdir


def bytes_conversion(bytes):
	if(bytes<1024):
		return str(bytes)+"bytes"
	elif(bytes>=1024 and bytes<=1024*1024):
		return str(bytes/1024.0) + "KB"
	else:
		return str(bytes/1024.0**2) + "MB"



def copy_func():
    source="C:\\Users\\29883\\Downloads\\software"
    dest = "E:\\"
    file_list = listdir(source)
    total_size_copied = 0 
    flag = 0
    while not flag:
    
	    for f in file_list:
	    	file_url = os.path.join(source,f)
	    	new_file_url = os.path.join(dest,f)
	    	i=0
	    	if(os.path.exists(new_file_url)):
	    		#print(file_url)
	    		#print("File already exists")
	    		f_name,extension = os.path.splitext(f)
	    		
	    		i=0
	    		new_f = f_name + "_"+ str(i) + extension
	    		renamed_dest_url = os.path.join(dest,new_f)
	    		
	    		while(os.path.exists(renamed_dest_url)):
	    			i = i + 1
	    			new_f = f_name + "_"+ str(i) + extension
	    			renamed_dest_url = os.path.join(dest,new_f)

	    		print("Copying to ...."+renamed_dest_url)
	    	
	    		try:
	    			shutil.copy(file_url,renamed_dest_url)
	    			file_size = os.stat(file_url).st_size
	    			total_size_copied = total_size_copied + file_size
	    			
	    		except IOError:
	    			#print "I/O error({0}):{1}".format(e.errno,e.strerror)
	    			print "IO error:Not enough space on pendrive "
	    			flag = 1
	    			break
	    		except:
	    			print "Unexpected error:",sys.exc_info()[0]
	    	else:
	    		try:
	    			shutil.copy(file_url,dest)
	    			file_size = os.stat(file_url).st_size
	    			total_size_copied = total_size_copied + file_size
	    			print("Copying "+ f + "to the pendrive")
	    		except IOError:
	    			#print "I/O error({0}):{1}".format(e.errno,e.strerror)
	    			print "IO error : Not enough space on prendrive"
	    			flag=1
	    			break 
	    		except:
	    			print "Unexpected error:",sys.exc_info()[0]
	    	
	    	print("Total file size copied till now "+bytes_conversion(total_size_copied))
    			


copy_func()