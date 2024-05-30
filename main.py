#this python script looks at a directory and deletes files in that directory that are older than 30 days

import os

directory = '/SPECIFY/YOUR/FOLDER/PATH/HERE' #this is the path to the directory i want to delete my old files in. you can figure it out by using the pwd command
print_commands = "find " + directory + " -mtime +30 -print" #this looks for and lists out the files what are older than 30 days
delete_commands = "find " + directory + " -mtime +30 -delete" #this looks for and deletes the files that are older than 30 days

os.system(print_commands) #this runs the above commands in the cli
os.system(delete_commands) #this runs the above commands in the cli
