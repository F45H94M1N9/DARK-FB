import os, sys

print ("\033[1;33mMasukan ID&PW :)")

print ("\033[1;33mTools Ini Ga Gratis ;)")
print ("\033[1;33mPM No 0895341201114")
ID = 'PCX'      
PW = 'PTX'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("ID : ")
	if uname == ID:
		pwd = raw_input("PW : ")

		if pwd == PW:
			print "\n\033[1;34mSelamat Datang", 
			sys.exit()

		else:
			print "\n\033[1;36mSorry Invalid PW !!!\033[00m"
			print "Back Login\n"
			restart()

	else:
		print "\n\033[1;36mSorry Invalid ID !!!\033[00m"
		print "Back Login\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
