#This script analyzes the '*.mdout' files and prints out the total energy
#python scriptname.py outputfilenmae.extension 

import os
import numpy as np
import argparse

#function_1 To open files and return all the lines in a variable
def open_mdout(filename):
    f=open(filename, 'r')
    data=f.readlines()
    f.close()
    return data

parser=argparse.ArgumentParser(description="This script analyzes the '*.mdout' files and prints out the total energy.")
parser.add_argument("mdout_file",help="This argument takes the name of the filename with mdout extension")
parser.add_argument("txt_file",help="This argument takes the name of the filename with txt extension i.e. to be written")
#Argument 1 for input filename and Argument 2 for output filename
#python scriptname.py --help prints the description and texts in help of the arguments
args=parser.parse_args()#The list stores the user given arguments i.e the path and filename

data=open_mdout(args.mdout_file)#Calling function_1 with the mdout filename which returns each line as an element in a list

f_write=open(args.txt_file,'w+')
f_write.write('Total Energy:\n')

for i in data:
    splitline=i.split()#splits data into different words(columns) in a list
    
    if 'Etot' in i:
        f_write.write(f'{splitline[2]}\n')

f_write.close()