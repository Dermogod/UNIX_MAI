import os
import subprocess

file_name = 'thread-'
path = '/home/lev/Desktop/MAI/' + file_name

bash_command = f"ls {file_name}* | wc -l"
output = os.popen(bash_command)
output = int(output.read())

for i in range(1, output + 1):
	with open(f"{path}" + str(i) + ".txt", 'r') as file:
		print(file.read())