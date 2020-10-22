import sys
import threading
import time
from colorama import Fore, Style


path = '/home/lev/Desktop/MAI/'
file = sys.argv[1]

with open(f"{path}" + file, 'r+') as fr:
	count = len(fr.readlines())
	txt = fr.readlines()

position = 0 
def worker(num):
	global position
	with open(f"{path}" + f"thread-{num + 1}.txt", 'w') as fw, \
	     open(f"{path}" + file, 'r+') as fr:
		print(f"{Fore.GREEN}{threading.current_thread().getName()} Starting{Style.RESET_ALL}")
		fr.seek(position)
		fw.write(fr.readline())
		position = fr.tell()
		print(threading.current_thread().getName(), 'Exiting')

try:
	for i in range(count):
		t = threading.Thread(name = f"Thread-{i+1}", target = worker, args = (i,), daemon = True)
		t.start()
		time.sleep(2.0)
except KeyboardInterrupt:
	print('Fine')
	sys.exit()