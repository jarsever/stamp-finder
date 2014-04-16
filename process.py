import os, sys, hashlib
from datetime import datetime


class Process():

	def __init__(self, B_Date, E_Date, F_Name):
		self.B_Date = datetime(B_Date[0],B_Date[1],B_Date[2])
		self.E_Date = datetime(E_Date[0],E_Date[1],E_Date[2])
		if F_Name[0] == '/':
			self.F_Name = os.path.basename(F_Name)
			self.F_Path = F_Name
		else:
			self.F_Name = os.path.basename(os.getcwd() + '/' + F_Name)
			self.F_Path = "{0}/{1}".format(os.getcwd(), F_Name)

		self.needs_hash = True
		self.md5 = ''
		self.sha1 = ''
		self.sha256 = ''

		self.create_files()
		self.hash()
		x = raw_input("Press Enter to continue...")
		self.hash()
		return


	def hash(self):

		if os.path.isfile(self.F_Path):
			f = open(self.Hash_Name, 'a')
		else:
			raise Exception("This is NOT a valid file: {0}".format(self.F_Path))

		data = file(self.F_Path).read(8192)
		print data

		f.write("===============================================================\n")

		if self.needs_hash == True:
			self.md5 = hashlib.md5(data).hexdigest()
			self.sha1 = hashlib.sha1(data).hexdigest()
			self.sha256 = hashlib.sha256(data).hexdigest()
			f.write("             This is the First time Hashing!\n")

		if self.needs_hash == False:
			if self.md5 == hashlib.md5(data).hexdigest():
				md5_match = True
			else:
				md5_match = False

			if self.sha1 == hashlib.sha1(data).hexdigest():
				sha1_match = True
			else:
				sha1_match = False

			if self.sha256 == hashlib.sha256(data).hexdigest():
				sha256_match = True
			else:
				sha256_match = False

			f.write("                  Finishing Hash Check\n")

		f.write("===============================================================\n\n")
		f.write("GENERATING HASHES FOR: {0}\n\n".format(self.F_Path))
		f.write("TIME: {0}\n\n".format(datetime.now()))
		f.write("MD5 => {0}\n".format(hashlib.md5(data).hexdigest()))
		f.write("SHA1 => {0}\n".format(hashlib.sha1(data).hexdigest()))
		f.write("SHA256 => {0}\n\n".format(hashlib.sha256(data).hexdigest()))

		if self.needs_hash == False:
			f.write("MD5 Pass: {0}\n".format(md5_match))
			f.write("SHA1 Pass: {0}\n".format(sha1_match))
			f.write("SHA256 Pass: {0}\n\n".format(sha256_match))

		f.write("\n")


		f.close()
		self.needs_hash = False


	def create_files(self):
		home = "{0}/Finder-Out".format(os.path.expanduser('~'))
		self.Hash_Name = "{0}/{1}_HASH".format(home, self.F_Name)
		self.Out_Name = "{0}/{1}_OUT".format(home, self.F_Name)
		print "Output Directory located at: {0}".format(home)
		if not os.path.exists(home):
			os.makedirs(home)

		if not os.path.isfile(self.Hash_Name):
			fh = open(self.Hash_Name, 'w')
			fo = open(self.Out_Name, 'w')
			fh.close()
			fo.close()


	def __str__(self):
		print (self.E_Date - self.B_Date).total_seconds()
		print ''
		print self.F_Name
		return ''

x = Process((1970,1,1), (2000,2,25), "time_stuff.py")
print x